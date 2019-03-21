# list1 = [i + 3 for i in range(5)]
# set1 = {i + 3 for i in range(5)}
# dict1 = {i: i + 3 for i in range(5)}
# print(list1, set1, dict1)
n = 10
a = [n for n in range(2, n+1) if all(n % i for i in range(2, n))]
print(a)
