def f1():
    x = 10

    def f11():
        return x

    def f12(n):
        nonlocal x
        x = n
    return f11, f12


getx, setx = f1()
print(getx())
setx(18)
print(getx())