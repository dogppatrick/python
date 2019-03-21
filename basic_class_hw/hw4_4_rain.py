import random
data_rain = []
for y in range(1, 5+1):
    rain_y = []
    for s in range(1, 4+1):
        rain_s = []
        for m in range(1, 3+1):
            # rain_s.append(random.uniform(0, 20))
            rain_s.append(random.randint(1, 5))
        rain_y = rain_y + [rain_s]
    data_rain = data_rain + [rain_y]
data_tmp = [[[2, 1, 3], [1, 1, 5], [3, 5, 4], [1, 1, 3]],
            [[4, 4, 1], [2, 3, 2], [5, 2, 1], [3, 4, 2]],
            [[2, 1, 2], [5, 4, 5], [5, 2, 5], [4, 3, 4]],
            [[5, 3, 4], [4, 4, 5], [5, 2, 2], [4, 4, 4]],
            [[2, 1, 1], [3, 4, 4], [2, 3, 3], [4, 3, 3]]]

def rain_f(key, od = 1):
    data_out = []
    data_tmp = [[[2, 1, 3], [1, 1, 5], [3, 5, 4], [1, 1, 3]],
                [[4, 4, 1], [2, 3, 2], [5, 2, 1], [3, 4, 2]],
                [[2, 1, 2], [5, 4, 5], [5, 2, 5], [4, 3, 4]],
                [[5, 3, 4], [4, 4, 5], [5, 2, 2], [4, 4, 4]],
                [[2, 1, 1], [3, 4, 4], [2, 3, 3], [4, 3, 3]]]
    y, s, m = len(data_tmp), len(data_tmp[0]), len(data_tmp[0][0])
    if key == "all":
        return data_tmp
    if key == "y":
        if od <= 5:
            od = od - 1
            return data_tmp[od]
    if key == "s":
        if od <= 4:
            od = od - 1
            for i in range(y):
                data_out.append(data_tmp[i][od])
        return data_out
    # month 1  [s=4][m=2]
    #       2  [s=4][m=3]
    #       3  [s=1][m=4]
    # if key == "month":
    #     if od <= 12:
    #         od = od - 1
    #         for i in range(y):
    #             data_out.append(data_tmp[i][od])
    #     return data_out

print(rain_f("s", 2))
