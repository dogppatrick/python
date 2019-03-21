list3 = [[[1, 2], [3, 4], [5, 6]], [[9, 8], [7, 6], [5, 4]]]

for i in range(len(list3)):
    for j in range(len(list3[i])):
        for k in range(len(list3[i][j])):
            print(list3[i][j][k], end="\t")
        print()
    print("===========")
