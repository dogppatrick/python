def sum_r(n):
    if n == 1:
        return 2
    if n <= 0:
        return 0
    return 2*n + sum_r(n-1)


# print(sum_r(1))