from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import warnings
import requests
import pandas as pd
warnings.filterwarnings("ignore")
# start connect
url = "https://www.ptt.cc/bbs/PC_Shopping/M.1552579550.A.CAF.html"
fn = "downloads/ptt_data/"
# r = Request(url)
# r.add_header("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
#                            "/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36")
response = requests.get(url)
html = BeautifulSoup(response.text)
# start ETL
content = html.find("div", id="main-content")
title_info = content.find_all("span", class_="article-meta-value")
title_tag = content.find_all("span", class_="article-meta-tag")
c = []
data_title = []
for i in range(len(title_info)):
    # print(title_tag[i].text, title_info[i].text)
    if i not in [0, 1, 2]:
        c .append(title_tag[i].text)
        data_title.append(title_info[i].text)
    # ptt id
    if i == 0:
        ptt_id = title_info[i].text
        c.append(title_tag[i].text)
        data_title.append(ptt_id.split(sep=" ")[0])
    # title
    if i == 2:
        a_title = title_info[i].text
        title_class = a_title[1:2+1]
        print(title_class)
        title_content = a_title[6:]
        print(title_content)
        c.append("分類")
        c.append("標題")
        data_title.append(title_class)
        data_title.append(title_content)
    title_info[i].extract()
    title_tag[i].extract()

push_info = content.find_all("div", class_="push")
push_data = {}
for i in range(len(push_info)):
    key = push_info[i].find("span", class_="push-userid").text
    value = push_info[i].find("span", class_="push-content").text
    if key in push_data:
        push_data[key] = push_data[key] + value
    else:
        push_data[key] = value
        fn = fn + "_" + value
# for key in push_data:
    # print(key, push_data[key])
c = c + ["url"]
# ['作者', '看板', '標題', '時間', 'url']
df = pd.DataFrame(columns=c)
s = pd.Series(data_title + [url], index=c)
df = df.append(s, ignore_index="true")
# # print(push_data)
# print(content.text)
df.to_csv("ptt_0315.csv", encoding="utf-8", index=False)
