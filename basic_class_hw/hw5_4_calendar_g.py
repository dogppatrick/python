def day_week_g():
    print("count year and week")


def p_c(week, days):
    # week = 0
    # days = [28, 29, 30, 31]
    week = week % 7
    raw_1 = ["日", "一", "二", "三", "四", "五", "六"]
    for mark in raw_1:
        print(mark, end="\t")
    print()
    c = 0
    for sp in range(week):
        print(end="\t")
        c = c + 1
    for i in range(1, days+1):
        print("%2d" % i, end="\t")
        c = c + 1
        if c % 7 == 0:
            print()


p_c(1, 31)
