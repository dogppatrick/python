T_pass = 123
ec = 0
while ec < 3:
    print("error time: ", ec)
    p = int(input("請輸入密碼\n"))
    if p == T_pass:
        ec = 10
    else:
        ec = ec + 1

if ec == 3:
    print("You fail")
else:
    print("Pass")
