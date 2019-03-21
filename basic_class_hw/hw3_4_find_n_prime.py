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


def f_n_prime(x):
    c = 1
    while x > 0:
        c = c+1
        if f_is_prime(c):
            x = x-1
    return c


# print(f_n_prime(25))
