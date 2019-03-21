def fe_f(n):
    n1 = 0
    n2 = 1
    for i in range(n+1):
        if i < 1:
            print(i, "\t", n1)
        else:
            ans = n1+n2
            print(i, "\t", n2)
            n1 = n2
            n2 = ans


fe_f(11)
