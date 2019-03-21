import math
# n = int(input("Input a N\n"))
for n in range(1, 100+1):
    tmp = 0
    for i in range(1, n):
        if math.gcd(n, i) == i:
            tmp = tmp + i
    if tmp == n:
        print(n)
    # else:
        # print("not %d" % n)

