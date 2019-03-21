class StackEmptyExcept(Exception):
    pass


class Stack1:
    def __init__(self):
        self.s = []

    def push(self, item):
        self.s = list(item) + self.s

    def pop(self):
        try:
            if len(self.s) == 0:
                raise StackEmptyExcept
            tmp = self.s[0]
            self.s.remove(tmp)
            return tmp
        except StackEmptyExcept:
            return "item null"

    def __str__(self):
        result = "["
        for i in range(len(self.s)):
            result = result + self.s[i]
            if i < len(self.s)-1:
                result = result + ","
        result = result + "]"
        return result


# def main():
#     s1 = Stack1()
#     print("p1:", s1)
#     s1.push("1")
#     s1.push("2")
#     print(s1)
#     s1.push("3")
#     s1.push("4")
#     print(s1.pop())
#     print(s1)
#     print(s1.pop())
#     print(s1.pop())
#     print(s1.pop())
#     print(s1.pop())
#     print(s1.pop())
#
#
# # main()
