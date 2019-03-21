b1 = int(input("使用家庭用電輸入 1，使用工業用電輸入 2\n"))
if b1 != 1 and b1 != 2:
    print("輸入錯誤")
else:
    d = int(input("請輸入使用度數\n"))
    if b1 == 2:
        print("您使用的為工業用電 %d 度 總計 %.2f元" % (d, d*0.45))
    else:
        if d <= 240:
            T_fee = d*0.15
        elif d <= 540:
            T_fee = 240*0.15+(d-240)*0.25
        else:
            T_fee = 240*0.15+(540-240)*0.25+(d-540)*0.45
        print("您使用的為家庭用電 %d 度 總計 %.2f元" % (d, T_fee))

print("感謝使用")
