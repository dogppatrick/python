# m = int(input("有多少錢ㄋ"))
m = 1500
print(m, "元 共找")
c_type = [1000, 500, 100, 50, 10, 5, 1]
you_get = []
for i in range(len(c_type)):
    if m >= c_type[i]:
        you_get.append(m//c_type[i])
        m = m % c_type[i]
    else:
        you_get.append(0)

for i in range(len(c_type)):
    print(c_type[i], "元", you_get[i], "個/張")
