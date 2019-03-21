y = 0
a = 100000
b = 100000
while a >= b:
    a = a+100000*0.1
    b = b*(1+0.05)
    y = y+1
print('year: %d ' % y)
print("A got: %d\t B got:%f " % (a, b))