w_hr = int(input("請輸入工作時數\n"))
if w_hr <= 60:
    pay = w_hr*120
elif w_hr <= 80:
    pay = 60*120+(w_hr-60)*120*1.25
else:
    pay = 60*120+20*120*1.5+(w_hr-80)*1.5
print("總共工作 %d 小時，薪資總共: %.2f " % (w_hr, pay))
