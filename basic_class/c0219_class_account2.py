# from forclass.c0214_class import Account
import forclass.c0214_class as A


class Account2(A.Account):
    def __init__(self, no, balance=0, c_limit=100):
        super(Account2, self).__init__(no, balance)
        self.c_limit = c_limit

    def wd(self, n):
        try:
            if n <= 0:
                raise ValueError
            self.balance = self.balance - n
            if self.balance - n < self.c_limit:
                print("over credit limit")
        except ValueError:
            print("value error")

    def __str__(self):
        return 'no: {0} balance: {1}'.format(self.no, self.balance)


def main():
    c1 = Account2(100, 1000, 100)
    print(c1.balance)


main()
