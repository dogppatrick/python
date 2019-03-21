import jieba
import jieba.analyse as jba
with open("t0305.txt", "r", encoding="utf-8") as f:
    article = ""
    read_a = f.readline()
    while read_a != "":
        if read_a != "\n":
            article = article + read_a
        read_a = f.readline()
# print(article)
jieba.load_userdict("dict.txt.big")
words = jieba.cut(article)
dict1 = {}
for word in words:
    if word in dict1:
        dict1[word] = dict1[word] + 1
    else:
        dict1[word] = 1
kw = jba.extract_tags(article, 15)
for i in range(len(kw)):
    print(kw[i], "wc:", dict1[kw[i]])

