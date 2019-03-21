import math
y = int(input("請輸入西元年\n"))

if int(math.fmod(y, 4)) != 0:
    print("不潤")
else:
    r = 1
    if int(math.fmod(y, 100)) == 0:
        r = 0
    if int(math.fmod(y, 400)) == 0:
        r = 1
    if int(math.fmod(y, 4000)) == 0:
        r = 0
    if r == 1:
        print("潤")
    else:
        print("不潤")
