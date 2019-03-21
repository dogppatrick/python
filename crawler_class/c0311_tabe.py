from urllib.request import urlopen
from bs4 import BeautifulSoup
import warnings
from urllib.error import HTTPError

import pandas as pd
c =["日文名稱", "評論數量", "消費估計_午", "消費估計_晚", "網頁連結"]
df = pd.DataFrame(columns=c)
warnings.filterwarnings("ignore")
pages = 58
while True:
    url = "https://tabelog.com/tw/tokyo/rstLst/" + str(pages) + "/?SrtT=rt"
    try:
        response = urlopen(url)
        print(url)
    except HTTPError:
        print("done")
        break
    html = BeautifulSoup(response)
    re_data = html.find_all("li", class_="list-rst")
    # print(re_data[0])
    for d in re_data:
        ja = d.find("small", class_="list-rst__name-ja")
        cms = d.find("a", class_="list-rst__reviews-target")
        cms_c = cms.find("b")
        costs = d.find_all("span", class_="c-rating__val")
        url_r = d.find("a", class_="list-rst__name-main js-detail-anchor")
        # print(ja.text, cms_c.text, costs[0].text, costs[1].text)
        s = pd.Series([ja.text, cms_c.text, costs[0].text, costs[1].text, url_r["href"]], index=c)
        df = df.append(s, ignore_index="true")
    pages = pages + 1
print(df)
# df.to_csv("tabelog.csv", encoding="utf-8", index=False)
