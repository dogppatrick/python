def sum_01(n, start=1):
    ans = 0
    for i in range(start, n+1):
        ans = ans + i
    avg = ans/n
    return n, ans, avg


# for a in [4, 5, 6, 100]:
#     print(sum_01(a))


def msg(st1, st2):
    print("%s and .... %s " % (st1, st2))


# msg("qqq", st2="wewewewe")
# msg(st2="wewewewe", st1="qqq")
def greet(*names):
    for name in names:
        print("YOOOOO", name)


# greet("aaa", "aaab", "noooooo")


def dic_kw(**data):
    for k, v in data.items():
        print("k=%s v=%s" % (k, v))


dic_kw(a1="11577", a2="wewewrt", a3="11111")
