list1 = [1, 2, 3, 4]
a1 = iter(list1)
print(next(a1))
print(a1.__next__(), "\n>>>>>")
while True:
    try:
        print(next(a1))
    except StopIteration:
        break
