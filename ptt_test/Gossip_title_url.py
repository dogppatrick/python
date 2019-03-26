# from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import warnings
import requests
import pandas as pd
warnings.filterwarnings("ignore")
start_page = 1
page = start_page
l_push = 10
b = False
df = pd.DataFrame(columns=["title", "author", "data", "url"])
while True:
    start_url = "https://www.ptt.cc/bbs/Gossiping/search?page=" + str(page) + "&q=recommend%3A" + str(l_push)
    url = start_url
    print(url)
    # r = Request(url)
    # r.add_header("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
    #                            "/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36")
    response = requests.get(url, cookies={"over18": "1"})
    html = BeautifulSoup(response.text)
    main_con = html.find("div", id="main-container")
    all_art = main_con.find("div", class_="r-list-container")
    art_box = all_art.find_all("div", class_="r-ent")
    for box in art_box:
        try:
            a_author = box.find("div", class_="meta").find("div", class_="author").text
            a_date = box.find("div", class_="meta").find("div", class_="date").text
            if a_date == " 3/20" or page-start_page >= 100:
                b = True
            if a_author not in "-":
                a_title = box.find("div", class_="title").text.strip()
                a_url = box.find("div", class_="title").find("a")["href"]
                a_url = "https://www.ptt.cc" + a_url
                data = a_title, a_author, a_date, a_url
                s = pd.Series(data, index=["title", "author", "data", "url"])
                df = df.append(s, ignore_index="true")
        except TypeError:
            print("error find")
            print(box.find("div", class_="title").text)
    page = page + 1
    if b:
        break
# print(articles[0])
# print(articles[0].text)
df.to_csv("gossip_10p_0326.csv", encoding="utf-8", index=False)
