def factor_01(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans * i
    return ans


for a in [4, 5, 6, 10]:
    print(factor_01(a))
