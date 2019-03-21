import random
c = 0
t = 1000
for mt in range(10):
    for i in range(t):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x*x+y*y <= 1:
            c = c+1

    print(c/t*4)
    c = 0
