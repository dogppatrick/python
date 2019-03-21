import urllib.request as urlr
import json
import os
url = "https://www.google.com/doodles/json/2019/2?hl=zh_TW"
path_dl = "D:/Python_crawler/Cawler36"
data_date = []
for m in range(1, 12+1):
    data_date.append(("2018", str(m)))
for m in range(1, 3+1):
    data_date.append(("2019", str(m)))

for y, m in data_date:
    url = "https://www.google.com/doodles/json/" + y + "/" + m + "?hl=zh_TW"
    path_save = path_dl + y
    if not os.path.exists(path_save):
        os.mkdir(path_save)
    path_save = path_save + "\\" + m
    if not os.path.exists(path_save):
        os.mkdir(path_save)
    path_save = path_save + "\\"
    resp = urlr.urlopen(url)
    data_jason = json.load(resp)
    for d in data_jason:
        url_1 = "http:" + d["url"]
        # print(url_1)
        fn = path_save + url_1.split("/")[-1]
        # print(fn)
        urlr.urlretrieve(url_1, fn)
        # print(url_1)

#
# resp = urlr.urlopen(url)
# data = json.load(resp)
# for d in data:
#     url = "http://" + d["url"]
#     print(url)