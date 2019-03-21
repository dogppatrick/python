def max_l(l):
    m = 0
    for i in range(len(l)):
        for j in range(len(l[i])):
            if i == 0 and j == 0 or m < int(l[i][j]):
                m = l[i][j]
    return m


def min_l(l):
    m = 0
    for i in range(len(l)):
        for j in range(len(l[i])):
            if i == 0 and j == 0 or m > int(l[i][j]):
                m = l[i][j]
    return m


def avg_l(l):
    total = 0
    c = 0
    for i in range(len(l)):
        for j in range(len(l[i])):
            total = total + l[i][j]
            c = c+1
    return total/c


def c_avg_l(l):

    c_avg = []
    for i in range(len(l)):
        total = 0
        c = 0
        for j in range(len(l[i])):
            total = total + l[i][j]
            c = c+1
        c_avg.append(total/c)
    return c_avg


def r_avg_l(l):
    r_total = []
    r_count = []
    r_avg = []
    for j in range(len(l[0])):
        r_total.append(0)
        r_count.append(0)
    for i in range(len(l)):
        for j in range(len(l[i])):
            r_total[j] = r_total[j] + l[i][j]
            r_count[j] = r_count[j] + 1
    for j in range(len(l[0])):
        r_avg.append(r_total[j]/r_count[j])
    return r_avg


L1 = [[7, 2, 3, 4], [13, 0, 6, 9], [6, 8, 9, 1]]
for q in range(len(L1)):
    print(L1[q])
print(avg_l(L1))    # a
print(max_l(L1))    # b
print(min_l(L1))    # c
print(c_avg_l(L1))  # d
# print(r_avg_l(L1))
