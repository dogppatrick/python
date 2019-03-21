# from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import warnings
import requests
from jieba.analyse import extract_tags
# import pandas as pd
# import jieba
# import jieba.analyse as jba
warnings.filterwarnings("ignore")
# start connect
url = "https://www.ptt.cc/bbs/Gossiping/M.1553004432.A.150.html"
response = requests.get(url, cookies={"over18": "1"})
# 如果你要純文字內容 .text
# 如果你不要他幫你解碼(圖片, 影片) .content
html = BeautifulSoup(response.text)
content = html.find("div", id="main-content")
metas = content.find_all("span", class_="article-meta-value")
print("ID:", metas[0].text)
print("看板:", metas[1].text)
print("標題:", metas[2].text)
print("時間:", metas[3].text)
# 盒子.extract()
metas = content.find_all("div", class_="article-metaline")
for m in metas:
    m.extract()
metas = content.find_all("div", class_="article-metaline-right")
for m in metas:
    m.extract()
pushes = content.find_all("div", class_="push")
score = 0
for p in pushes:
    tag = p.find("span", class_="push-tag")
    if "推" in tag.text:
        score = score + 1
    elif "噓" in tag.text:
        score = score - 1
    p.extract()
print("分數:", score)
# print("內容:", content.text)
print("重點:", extract_tags(content.text, 15))
