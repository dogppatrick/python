x = '10'

def fun_1():
    x = '87'
    print("fun_1 "+x)
    def fun_1_1():
        x = "69"
        print("fun_1_1 "+x)
    fun_1_1()
    print("fun_1 2 "+x)


fun_1()
print(x)
