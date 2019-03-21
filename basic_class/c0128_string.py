# a = "aaaabcdefg"
# b = "aa" in a
# print(b)
# for k in a:
#     print(k, end="\t")
# print()
# print(a[1:3])
#
# a = "87"
# print(a*2)
# a = "1 23 456 78 9 10"
# print(a.split())
# str1 = "aaa bbb ccc"
# print(str1.split(' '))
str1 = "aaab1s"
print(str1.isalnum())
print(str1.isalpha())  # all char
print(str1.isdigit())  # all num
print(str1.islower())
print()
a = ">cc  <"
print(a.isspace())
print(a.startswith(" "))
print()
b = "123456789abcdee1fg"
c = "012345678901234567"
print(b.rfind("1"))
print("|"+a.center(7)+"|")
