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


# for i in range(1, 30):
#     if (f_is_prime(i)):
#         print("%d\t%s" % (i, f_is_prime(i)))
