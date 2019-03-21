season = int(input('輸入月份1~12月\n'))

if 3 <= season <= 5:
    print('%d月 94 春天' % season)
elif 6 <= season <= 8:
    print('%d月 94 夏天' % season)
elif 9 <= season <= 11:
    print('%d月 94 秋天' % season)
elif season == 12 or 1 <= season <= 2:
    print('%d月 94 冬天' % season)
else:
    print("輸入錯誤")
