import random


def id_g(area_code, gender):
    c_list = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L",
              "M", "N", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "W", "Z", "I", "O"]
    c_num = list(range(10, 37))
    check = c_list.index(area_code)
    check = c_num[check]
    check = divmod(check, 10)[0] + divmod(check, 10)[1]*9 + gender * 8
    new_id = area_code + str(gender)
    for i in range(8, 1, -1):
        rd_n = random.randint(0, 9)
        new_id = new_id + str(rd_n)
        check = check+rd_n*(i-1)
    checkid = divmod(10-divmod(check, 10)[1], 10)[1]
    new_id = new_id + str(checkid)
    return new_id


print(id_g("A", 2))
