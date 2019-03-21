class Account:
    def __init__(self, no, balance=0):
        self.no = no
        self.balance = balance

    def dp(self, n):
        try:
            if n <= 0:
                raise ValueError
            self.balance = self.balance + n
        except ValueError:
            print("value error")

    def wd(self, n):
        try:
            if n <= 0:
                raise ValueError
            self.balance = self.balance - n
        except ValueError:
            print("value error")

    def __str__(self):
        return 'no: {0} balance: {1}'.format(self.no, self.balance)


# def main():
#     # acc1 = Account(9487, 1)
#     # print("no : ", acc1.no)
#     # print("balance:", acc1.balance)
#     # acc1.dp(500)
#     # print("balance:", acc1.balance)
#     # acc1.wd(50)
#     # print("balance:", acc1.balance)
#     # acc2 = Account(9887, 10000)
#     # print("acc2 balance", acc2.balance)
#     # print(acc2)
#     # acc_list = [Account("001", 100), Account("002", 150), Account("003", 200)]
#     # for acc in acc_list:
#     #     print(acc)
#
#
# main()
