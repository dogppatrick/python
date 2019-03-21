print("\t|\t", end="")
for i in range(1, 9+1):
    print("%d \t" % i, end="")
print()
print("--------------------------------------------")
for i in range(9, 0 , -1):
    print("%d\t|\t" % i, end="")
    for j in range(1, 9+1):
        # if i == 1:
        #     print("  ", end="")
        if(i >= j):
            print('%d\t' % (i*j), end="")
    print()

