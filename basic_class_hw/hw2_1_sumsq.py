total = 0
for i in range(1, 50+1):
    if divmod(i, 2)[1] == 1:
        total = total + i**2
        # print("plus %d" % i)
    else:
        total = total - i**2
        # print("minus %d" % i)
print("ans= %d " % total)
