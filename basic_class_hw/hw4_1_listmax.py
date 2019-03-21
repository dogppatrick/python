def max_l(l):
    m = 0
    if ~isinstance(l[0], list):
        l = [l]
    for i in range(len(l)):
        for j in range(len(l[i])):
            if i == 0 and j == 0 or m < int(l[i][j]):
                m = l[i][j]
    return m


def min_l(l):
    m = 0
    if ~isinstance(l[0], list):
        l = [l]
    for i in range(len(l)):
        for j in range(len(l[i])):
            if i == 0 and j == 0 or m > int(l[i][j]):
                m = l[i][j]
    return m


L = [1, 2, 3, 4, 5, 9, 10, 7]
print(max_l(L))
