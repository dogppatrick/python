import random


def g_num(n1=1, n2=100):
    ans = random.randint(n1, n2)
    if n1 > n2:
        tmp = n2
        n2 = n1
        n1 = tmp
    while True:
        print("Guest a n from", n1, "to", n2)
        g = int(input())
        if g == ans:
            print("Win")
            break
        elif n2 > g > ans:
            n2 = g
            print("Too big")
        elif ans > g > n1:
            n1 = g
            print("Too small")
        else:
            print("out of range")


g_num()
