import pandas as pd
import numpy as np
import glob
import os
import time
path = os.path.abspath("")+"/"
print(path)
fn_list = glob.glob(path + "/input_resource/*.csv")
# print(fn_list)
fn_to_save = ["fc_die.csv", "fc_may_die.csv", "fc_live.csv"]
# edit info :	 31-MAR-19
# data_source\全國營業(稅籍)登記(停業)資料集.csv to fc_die.csv done
# edit info :	 01-MAR-19
# data_source\全國營業(稅籍)登記(停業以外之非營業中)資料集.csv to fc_may_die.csv done
# edit info :	 31-MAR-19
# data_source\全國營業(稅籍)登記資料集.csv to fc_live.csv done
# loading  save append count
c = 0
find_list = ["花店", "花卉", "鮮花", "盆栽", "園藝"]
for q in range(len(fn_list)):
    data_w = ""
    fn_load = fn_list[q]
    fn_save = fn_to_save[q]
#     delete data if exist
    if os.path.exists(fn_save):
        os.remove(fn_save)
        print("delete exist data")
    # print(fn_load)
    with open(fn_load, "r", encoding="utf-8") as f:
        data = f.readline()
    #     add title
        data_w = data_w + data
        data = f.readline()
        # print("edit info :\t", data)
        while data != "":
            data = f.readline()
            if any(item in data for item in find_list):
                data_w = data_w + data
                c = c + 1

            if ((c+1) % 100000) == 0:
                with open(fn_save, "a", encoding="utf-8") as fr:
                    fr.write(data_w)
                    data_w = ""
                    print("data_saved")
        with open(fn_save, "a", encoding="utf-8") as fr:
            fr.write(data_w)
    # print(fn_list[q], "to", fn_to_save[q], "done")
# fn_list = glob.glob("data_source/*.*")
# print(fn_list)
fn_to_save = ["fc_die.csv", "fc_live.csv"]
for q in range(len(fn_to_save)):
    fn = fn_to_save[q]
    # print(fn)
    data = pd.read_csv(path + fn, encoding="utf-8")

    # data
    # print(fn)
    # 新增 arr_d type np.array 用於計算
    arr_d = np.array(data)
    # c = 個別欄位名稱
    c = data.columns.tolist()
    # for i in range(len(c)):
        # print(c[i], i, end="\t")
        # print(arr_d[0:10, i])
    data_raws = data.shape[0]
    # 行業代號
    b_c = np.array(list(range(8, 14+1, 2)))
    # 名稱
    b_n = np.array(list(range(9, 15+1, 2)))
    bs_code_new = []
    bn_code_new = []
    t1 = time.time()
    for i in range(data_raws):
        # l = 行業代號 去除nan 轉為int
        l = arr_d[i, b_c]
        l = l[~pd.isna(l)]
#         l = l.astype(int)
        bs_code_new.append(l.astype(int).__str__())
        # l = 名稱 去除nan
        l = arr_d[i, b_n]
        l = l[~pd.isna(l)]
        bn_code_new.append(l.__str__())
    # print(time.time()-t1)
#     print(bs_code_new,bn_code_new)
    data["行業代碼_new"]=bs_code_new
    data["名稱_new"]=bn_code_new
    data = data.drop(['名稱', '名稱1', '名稱2', '名稱3', '行業代號',
                      '行業代號1', '行業代號2', '行業代號3', '總機構統一編號'], axis=1)
    fn = "recode_" + fn
    data.to_csv(path + fn, index=False, encoding="utf-8")
    # print("data saved", fn)

fn_to_save = ["fc_may_die.csv"]
for q in range(len(fn_to_save)):
    fn = fn_to_save[q]
    data = pd.read_csv(path + fn, encoding="utf-8")
    # data
    # 新增 arr_d type np.array 用於計算
    arr_d = np.array(data)
    # c = 個別欄位名稱
    c = data.columns.tolist()
    # for i in range(len(c)):
    #     print(c[i],i, end="\t")
    #     print(arr_d[0:10,i])
    data_raws = data.shape[0]
    # 行業代號
    b_c = np.array(list(range(7, 13+1, 2)))
    # 名稱
    b_n = np.array(list(range(8, 14+1, 2)))
    bs_code_new = []
    bn_code_new = []
    t1 = time.time()
    for i in range(data_raws):
        # l = 行業代號 去除nan 轉為int
        l = arr_d[i,b_c]
        l = l[~pd.isna(l)]
#         l = l.astype(int)
        bs_code_new.append(l.astype(int).__str__())
        # l = 名稱 去除nan
        l = arr_d[i, b_n]
        l = l[~pd.isna(l)]
        # print(l, l.__str__())
        bn_code_new.append(l.__str__())
    # print(time.time()-t1)
    # print(bs_code_new,bn_code_new)
    data["行業代碼_new"] = bs_code_new
    data["名稱_new"] = bn_code_new
    data = data.drop(['名稱', '名稱1', '名稱2', '名稱3', '行業代號',
                      '行業代號1', '行業代號2', '行業代號3', '總機構統一編號'], axis=1)
    fn = "recode_" + fn
    data.to_csv(fn, index=False, encoding="utf-8")
    # print("data saved", fn)

fn_list = glob.glob(path + "/recode_*")
# print(fn_list)
# print("========q=q=q=q")
datas =[]
for fn in fn_list:
    # print(fn)
    print(fn)
    datas.append(pd.read_csv(fn, encoding="utf-8"))
data_code = ["die", "live", "may_die"]
arr_data = []
for data in datas:
    print("===========")
#     print(data)
    arr_data.append(np.array(data).astype(str))
# arr_data
nraw = []
for j in range(3):
    # print("*****"+data_code[j]+"*****")
    c = datas[j].columns.tolist()
    # for i in range(len(c)):
        # print(c[i], i, end="\t")
        # print(arr_data[j][0:3, i])
    nraw.append(datas[j].shape[0])
# print(len(datas))
uid = []
for i in range(3):
    uid_c = np.array(datas[0]["統一編號"]).astype(str)
#     print(uid_c)
    uid.append(uid_c)

# fix data in each two file
compare_uuid = {}
for i in range(3):
    for j in range(3):

        if i < j:
            comp=data_code[i] + " vs " + data_code[j]
            compare_uuid[comp] = list(np.intersect1d(uid[i], uid[j]))
# for key in compare_uuid:
#     print(key, len(compare_uuid[key]), compare_uuid[key])
# print(len(compare_uuid))

din2 = []
for i in range(nraw[0]):
    id = str(arr_data[0][i, 1])
    if id in compare_uuid["die vs may_die"]:
        din2.append(arr_data[0][i, :])
        # print(arr_data[0][i, :])
df0 = pd.DataFrame(din2, columns=datas[0].columns.tolist())

din2 = []
for i in range(nraw[2]):
    id = str(arr_data[2][i, 1])
    if id in compare_uuid["live vs may_die"]:
        din2.append(arr_data[2][i, :])
df0 = pd.DataFrame(din2, columns=datas[2].columns.tolist())
# print(data_code[2])


# drop weight die > may_die > live
# data_code=["die", "live", "may_die"]
idx_rm =[]
for id in compare_uuid["die vs may_die"]:
    idx_rm.append(np.nonzero(arr_data[2][:, 1] == int(id)))
arr_data[2] = np.delete(arr_data[2], idx_rm, 0)
for id in compare_uuid["live vs may_die"]:
    idx_rm.append(np.nonzero(arr_data[1][:, 1] == int(id)))
arr_data[1] = np.delete(arr_data[1], idx_rm, 0)


# a = (arr_data[0][:,1], arr_data[0][:,3]) <<tuple
target_c = ['統一編號', '營業人名稱', '資本額', '使用統一發票', '行業代碼_new', '名稱_new',
            '設立日期', '停業日期', '組織別名稱','營業地址']
rsp_arr = []
for i in range(3):
    re_c = np.array(datas[i].columns.tolist())
#     print(re_c)
    idx_c = []
    lost_c = []
    for j in range(len(target_c)):
        if target_c[j] in list(re_c):
            idx_c.append(np.nonzero(re_c == target_c[j])[0][0])
#             print(idx_c[j], target_c[j])
        else:
            idx_c.append(-1)
            lost_c.append(target_c[j])
    print("lost_c:", lost_c)
    rsp = []
    c1 = []
    lost = 0
#     print("save")
    for j in range(len(target_c)):
        if idx_c[j] != -1:
            rsp.append(datas[i][re_c[idx_c[j]]])
            c1.append(re_c[idx_c[j]])
        else:
            rsp.append(np.repeat(0, len(datas[i])))
            c1.append(lost_c[lost])
            lost = lost +1
    # print(tuple(rsp))
    rsp_done = np.column_stack(tuple(rsp))
    rsp_arr.append(rsp_done)


arr_merge = np.concatenate(tuple(rsp_arr), axis=0)
merge_df = pd.DataFrame(arr_merge, columns=c1)

merge_df.to_csv("flower_business_merge.csv", index=False, encoding="utf-8")

from collections import Counter

df = merge_df
# df = pd.read_csv("../result/flower_business_merge.csv", encoding="utf-8", sep=",")
c1 = df["名稱_new"]
nraw = len(c1)
# b:殯葬 r:餐廳 s:花卉相關銷售 g:花卉栽種 d: 丟棄
tag_data = []
d_idx = []
b_tag = "'殯葬禮儀服務' '其他殯葬服務' '宗教、喪葬用品零售'".replace("\'", "").split(" ")
r_tag = "'餐館、餐廳'".replace("\'", "").split(" ")
s_tag = "'花卉材料、園藝器具零售' '種苗批發' '園藝苗木零售' '切花、盆栽批發' '切花、盆栽零售' '農產品（花卉）批發市場承銷'".replace("\'", "").split(" ")
g_tag =  "'其他花卉栽培'  '盆景栽培' '綠化服務' '庭園景觀工程'".replace("\'", "").split(" ")
for i in range(nraw):
    tags = c1.iloc[i].replace("[", "").replace("]", "").replace("\'", "").split(" ")
#     print(tags)
    result = [0, 0, 0, 0, 0]
    for tag in tags:
        if tag in b_tag:
            result[0] = 1
        if tag in r_tag:
            result[1] = 1
        if tag in s_tag:
            result[2] = 1
        if tag in g_tag:
            result[3] = 1
        if any(result):
            result[4] = 1
    if result[4]:
        result[4] = 0
    else:
        result[4] = 1
        d_idx.append(i)
    tag_data.append(result)
#     print(result)
tag_data = np.asarray(tag_data)

t = ["殯葬", "餐廳",  "花卉相關銷售",  "花卉栽種",  "丟棄"]
for i in range(4):
    df[t[i]] = tag_data[:, i]
df = df.drop(columns=["行業代碼_new", "名稱_new"])
df = df.drop(d_idx, axis=0)
# 清除 tag > 新增相關 tag

cond_b = df["組織別名稱"]
date = df["設立日期"]
date = np.array(date) + 19110000
date = date.astype(str)
date_1 = []
for i in range(len(date)):
    d_y = date[i][0:4]
    d_m = date[i][4:6]
    d_d = date[i][6:8]
    if d_d == "00":
        d_d = "01"
        # print(i)
        # print(df.iloc[i])
    d = d_y + "-" + d_m + "-" + d_d
    date_1.append(d)
date = df["停業日期"]
date = np.array(date) + 19110000
date = date.astype(str)
date_2 = []
for i in range(len(date)):
    d_y = date[i][0:4]
    d_m = date[i][4:6]
    d_d = date[i][6:8]
    d = d_y + "-" + d_m + "-" + d_d
    if d_d != "00" and d_m == "00":
        print("===")
        print(i)
        print(df.iloc[i])
#     print(d)
    if date[i] == "19110000":
        date_2.append("n")
    else:
        date_2.append(d)
# print(date_2)
# df = pd.read_csv("flower_business_with_type.csv")
arr = np.array(df)
nraw = len(arr)

curr_st = []
for i in range(nraw):
    d = arr[i, :]
    if d[6] != 0:
        curr_st.append("alive")
    elif d[5] == 0:
        curr_st.append("close")
    else:
        curr_st.append("die")
df["curr_stat"] = curr_st

df.to_csv("flower_business_with_type.csv", index=False, encoding="utf-8")
