from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import warnings
import requests
import pandas as pd
import math
warnings.filterwarnings("ignore")
# start connect
# load csv
gossip_url = pd.read_csv("gossip_10p_0326.csv", sep=",", encoding="utf-8")
# for i in range(gossip_url.__len__()):
data_c = ["uuid", "a_id", "a_data", "p_id", "push_c"]
# # ['作者', '看板', '標題', '時間', 'url']
df = pd.DataFrame(columns=data_c)

for i in range(gossip_url.__len__()):
    url = gossip_url.iloc[i, 3]
    # if i % 30 == 0:
    #     print(url, i, "done")
    a_author = gossip_url.iloc[i, 1]
    a_id = url[33:-5]
    a_data = gossip_url.iloc[i, 2]
    a_info = [a_id, a_author, a_data]
    response = requests.get(url, cookies={"over18": "1"})
    html = BeautifulSoup(response.text)
    # start ETL

    try:
        content = html.find("div", id="main-content")
        # print(content)
        push_info = content.find_all("div", class_="push")
        push_data = {}
        for j in range(len(push_info)):
            key = push_info[j].find("span", class_="push-userid").text
            if key in push_data:
                push_data[key] = push_data[key] + 1
            else:
                push_data[key] = 1
        # print(push_data)
        for key in push_data:
            data_collect = a_info + [key, round(1 + math.log10(push_data[key]), 2)]
            s = pd.Series(data_collect, index=data_c)
            df = df.append(s, ignore_index="true")
    except AttributeError:
        print("error find")
        print(url)

    # savefile
    if i+1 % 50 == 0:
        df.to_csv("push_data_0326.csv", encoding="utf-8", index=False, mode="a")
        df = pd.DataFrame(columns=data_c)
        print("data_saved", i, url)
df.to_csv("push_data_0326.csv", encoding="utf-8", index=False, mode="a")
