class Emp:
    def __init__(self, name, e_date, phone, address, base_s=50000):
        self.name = name
        self.e_date = e_date
        self.phone = phone
        self.address = address
        self.base_s = base_s
        self.salary = 0
        self.e_hour = 0
        self.c_salary()

    def c_salary(self):
        self.salary = int(self.base_s + self.base_s/240*1.5*self.e_hour)

    def __str__(self):
        self.c_salary()
        return "Employee name :{}\tE_date:{}\tPhone:{}\tAddress:{}\nSalary:{}".\
            format(self.name, self.e_date,self.phone, self.address, self.salary)


class Manager2(Emp):
    def c_salary(self):
        self.salary = int(self.base_s + self.base_s / 240 * 1.5 * self.e_hour)+1800+3000


class Ceo(Emp):
    def c_salary(self):
        self.salary = int(self.base_s + self.base_s / 240 * 1.5 * self.e_hour)+1800+2000+5000


def main():
    e1 = Emp("emp1", "2009-1-1", "000", "bbbb", 36000)
    ceo = Ceo("ceo1", "2000-1-1", "000", "cccc", 70000)
    m1 = Manager2("manager1", "2005-1-1", "222", "qqqqq", 55000)
    ceo.e_hour = 10
    m1.e_hour = 10
    e1.e_hour = 30
    print(e1)
    print(m1)
    print(ceo)


# main()
