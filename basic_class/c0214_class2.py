class G:
    def m1(self):
        print("G1.m1")


class P1(G):
    def m2(self):
        print("P1.m2")


class P2:
    def m2(self):
        print("P2.m2")

    def m1(self):
        print("P2.m1")


class C(P1, P2):
    def m3(self):
        print("C.m3")


def main():
    c = C()
    c.m1()
    c.m2()
    c.m3()


main()
