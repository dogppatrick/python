yd = False
while True:
    try:
        a = int(input("input int\n"))
        if a == 64:
            raise ValueError
        if a == 87:
            raise EOFError
        if a == 0:
            raise IOError
        print(a)
    except ValueError as error1:
        print("we .... him/her")
        break
    except EOFError as error:
        print("error2")
        break
    else:
        print("eeeeeeeeeeeeeeeeeeeeeeee")
        break
    finally:
        print("end...")
