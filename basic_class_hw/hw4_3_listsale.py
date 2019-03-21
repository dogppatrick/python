def f_sale_g(list_all):
    col_c = len(list_all[0])
    raw_c = len(list_all)
    p = []
    sale_r = []
    data_s = []
    data_p = []
    # print(col_c)
    # print(raw_c)
    for i in range(1, raw_c):
        sale_r.append(list_all[i][0])
        data_s.append([])
    for j in range(1, col_c):
        p.append(list_all[0][j])
        data_p.append([])
    for i in range(1, raw_c):
        for j in range(1, col_c):
            data_s[i - 1].append(list_all[i][j])
    for i in range(1, col_c):
        for j in range(1, raw_c):
            data_p[i - 1].append(list_all[j][i])
    return p, sale_r, data_s, data_p


def pd_s(pd_c, pd_price):
    total = 0
    for i in range(len(pd_c)):
        total = total + int(pd_c[i])*pd_price
    return total


def top_pd(pd, data_p, pd_price):
    top_pd = ""
    top_sum = 0
    total_sum = []
    for p_i in range(len(pd)):
        pd_c = 0
        for i in range(len(data_p[p_i])):
            pd_c = pd_c + int(data_p[p_i][i])
        total_sum.append(pd_c*pd_price[p_i])
        if top_sum <= pd_c*pd_price[p_i]:
            top_sum = pd_c*pd_price[p_i]
            top_pd = pd[p_i]
    return top_pd


def top_sale_er(sale_r, data_s, pd_price):
    top_saler = 0
    top_sum = 0
    total_sum = []
    for s_i in range(len(sale_r)):
        total_sum.append(0)
        for s_j in range(len(data_s[s_i])):
            total_sum[s_i] = total_sum[s_i] + int(data_s[s_i][s_j]) * pd_price[s_i]
        if top_sum <= total_sum[s_i]:
            top_sum = total_sum[s_i]
            top_saler = s_i
    return sale_r[top_saler]


sale = [["銷售員", "pA", "pB", "pC", "pD", "pE"], ["Jean", "33", "32", "56", "45", "33"],
        ["Tom", "77", "33", "68", "45", "23"], ["Tina", "43", "55", "43", "67", "65"]]
pd_price = [12, 16, 10, 14, 15]
pd, sale_r, data_s, data_p = f_sale_g(sale)
print("Top sales :", top_sale_er(sale_r, data_s, pd_price))
print("Top production :", top_pd(pd, data_p, pd_price))
# print(pd_s(data_p[0], pd_price[0]))

# for i in range(len(pd)):
#     print("%s sales total = %d" % (pd[i], pd_s(data_p[i], pd_price[i])))
