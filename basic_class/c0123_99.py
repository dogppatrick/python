for i in range(1,9+1):
    for j in range(1,9+1):
        print("%d X %d = %d\t" % (i, j, i*j), end="")
    print()
print()
for i in range(1,9+1):
    for j in range(1,9+1):
        print("%d X %d = %d\t" % (j, i, i*j), end="")
    print()