import math
total = 0
n = 1
for i in range(10):
    total = total + n
    n = n+1
print(total)
total = 0
n = 1
while n < 100:
    if math.fmod(n, 2) == 1:
        total = total + n
        # print(n)
    n = n+1
print(total)
while 1:
    if math.fmod(n, 2) == 1:
        total = total + n
        # print(n)
    n = n+1
    if n >= 100:
        break
