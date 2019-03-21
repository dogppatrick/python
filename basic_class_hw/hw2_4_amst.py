for n in range(100, 999+1):
    a = divmod(n, 100)[0]
    b = divmod(divmod(n, 100)[1], 10)[0]
    c = divmod(n, 10)[1]
    if a**3+b**3+c**3 == n:
        print(n)
