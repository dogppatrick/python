def id_c_check(id_c):
    c_list = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L",
              "M", "N", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "W", "Z", "I", "O"]
    c_num = list(range(10, 37))
    # id_c = "J122666663"
    #         0123456789
    if id_c[0] not in c_list:
        return "Area code error"
    if int(id_c[1]) not in [1, 2]:
        return "Gender code error"

    check = c_num[c_list.index(id_c[0])]
    check = divmod(check, 10)[0]*1 + divmod(check, 10)[1]*9
    for i in range(1, 8 + 1):
        check = check + int(id_c[i]) * (9 - i)
    if divmod(divmod(check, 10)[1]+int(id_c[9]), 10)[1] != 0:
        return "Check id_c error"
    return "is ID"


print(id_c_check("A255956925"))
