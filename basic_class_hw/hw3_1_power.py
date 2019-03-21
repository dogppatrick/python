def power_01(n, p):
    ans = 1
    for i in range(p):
        ans = ans * n
    return ans


# print(power_01(2, 3))
