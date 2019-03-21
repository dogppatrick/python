def f_b(n):
    ans = ""
    while n > 1:
        ans = str(divmod(n, 2)[1])+ans
        n = divmod(n, 2)[0]
    ans = str(divmod(n, 2)[1]) + ans
    return ans


def f_h(n):
    ans = ""
    simbo_h = ["A", "B", "C", "D", "E", "F"]
    while n > 15:
        add_d = str(divmod(n, 16)[1])
        if int(add_d) >= 10:
            add_d = simbo_h[int(add_d)-10]
        ans = add_d+ans
        n = divmod(n, 16)[0]
    add_d = str(divmod(n, 16)[1])
    if int(add_d) >= 10:
        add_d = simbo_h[int(add_d) - 10]
    ans = add_d + ans
    return ans


for i in range(1, 40):
    print(f_h(i)+"\t"+str(i))
