import math
n = int(input("Input a N\n"))

for i in range(1, n+1):
    if math.gcd(n, i) == i:
        print("%d \t" % i, end="")
