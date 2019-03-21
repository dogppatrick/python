# with open("t0219.txt", "r") as f:
#     line = f.readline()
#     while line != "":
#         print(line, end="")
#         line = f.readline()
#
# print()
# with open("t0219.txt", "r") as f:
#     line = f.readline()
#     while line != "":
#         print(repr(line))
#         line = f.readline()
#
# with open("t0219.txt", "r") as f:
#     all_line = f.read()
#     print(repr(all_line))
#

with open("t0219.txt", "rb") as f:
    all_line = f.read()
    print(repr(all_line))
    print()
    f.seek(3)
    f.seek(1, 1)
    all_line = f.read()
    print(repr(all_line))
