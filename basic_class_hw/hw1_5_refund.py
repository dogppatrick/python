cost = int(input("輸入商品售價\n"))
pay = int(input("輸入實際付出金額\n"))
T_d = Ft_d = F_d = B_d = Tt_d = Fd_d = 0
if cost > pay:
    print("金額不足")
elif cost == pay:
    print("剛剛好r")
else:
    rem = pay - cost
    if rem >= 1000:
        T_d = divmod(rem, 1000)[0]
        rem = divmod(rem, 1000)[1]
    if rem >= 500:
        F_d = divmod(rem, 500)[0]
        rem = divmod(rem, 500)[1]
    if rem >= 100:
        B_d = divmod(rem, 100)[0]
        rem = divmod(rem, 100)[1]
    if rem >= 50:
        Ft_d = divmod(rem, 50)[0]
        rem = divmod(rem, 50)[1]
    if rem >= 10:
        Tt_d = divmod(rem, 10)[0]
        rem = divmod(rem, 10)[1]
    if rem >= 5:
        Fd_d = divmod(rem, 5)[0]
        rem = divmod(rem, 5)[1]

    print('找你...%d張千元 %d張五百元 %d 張一百元 %d 個50 元 %d 個 十元 %d 個五元 還有%d元' % (T_d, F_d, B_d, Ft_d, Tt_d, Fd_d, rem))
