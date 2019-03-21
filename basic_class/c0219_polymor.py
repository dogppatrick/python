class C1:
    def run(self):
        print("c1.run")


class C2:
    def run(self):
        print("c2.run")


def run_m(c):
    c.run()


def main():
    c1 = C1()
    c2 = C2()
    run_m(c1)
    run_m(c2)


main()
