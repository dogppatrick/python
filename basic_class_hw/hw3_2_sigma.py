def pw1(n, p):
    ans = 1
    for i in range(p):
        ans = ans * n
    return ans


def fac1(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans * i
    return ans


def sig(x, n):
    ans = 0
    for i in range(1, n+1):
        ans = ans + (pw1(x, i)/fac1(i))
        # print(i, end="\t")
        # print(pw1(x, i)/fac1(i))

    return ans


# print(sig(2, 4))
