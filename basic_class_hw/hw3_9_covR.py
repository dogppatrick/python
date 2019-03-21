def f_h2(n):
    n = int(n)
    s_h = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    if divmod(n, 16)[0] == 0:
        return s_h[divmod(n, 16)[1]]
    else:
        return str(f_h2(divmod(n, 16)[0]))+s_h[divmod(n, 16)[1]]


def f_b2(n):
    n = int(n)
    if divmod(n, 2)[0] == 0:
        return str(divmod(n, 2)[1])
    else:
        return str(f_b2(divmod(n, 2)[0]))+str(divmod(n, 2)[1])


for i in range(1, 30):
    print("%d\t%s\t\t%s" % (i, f_b2(i), f_h2(i)))


