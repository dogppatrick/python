import math
n = int(input("Input N\n"))

for i in range(2, n+1):
    if i > 2 and divmod(i, 2)[1] == 0:
        continue
    else:
        p = 1
        for j in range(1, int(i/2)):
            if math.gcd(i, j) != 1:
                p = 0
        if p == 1:
            print(i, end="\t")
