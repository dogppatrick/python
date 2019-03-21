def f_is_prime(n):
    import math
    if n != 2 and divmod(n, 2)[1] == 0 or n == 1:
        return False
    else:
        p = 1
        for j in range(1, int(n / 2)):
            if math.gcd(n, j) != 1:
                    p = 0
        if p == 1:
            return True
        else:
            return False


def f_is_2np(n):
    b = 2
    while n > b:
        b = b*2
    if n == (b-1):
        return True
    else:
        return False


def mersenne(n):
    if f_is_2np(n) and f_is_prime(n):
        return True
    else:
        return False


# for i in range(20):
#     print(str(i)+"\t"+str(mersenne(i)))
# for i in range(500):
#     if mersenne(i):
#         print(i, end="\t")
