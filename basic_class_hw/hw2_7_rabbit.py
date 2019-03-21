r = 1
while 1:
    if divmod(r, 3)[1] == 1 and divmod(r, 5)[1] == 3 and divmod(r, 7)[1] == 2:
        print(r)
        break
    r = r+1
