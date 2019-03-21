# print(r"test/c0107.py")
# print("test\\test\"test\ntest\ttest\'test")
# for a in range(1, 10):
#    print(~a, a, a + ~a)

print(9//4)
print(9 % 4)
print(r"9 // -4 = ", 9 // -4)
print(r"9 % -4 = ", 9 % -4)

# a = 1
# b = 1
# print(a is b)
# print('下午%02d時:%2d分' % (1, 55))

x = 3184
print('%X' % x)
print('%#X' % x)
print('%+X' % x)
print('%#o' % x)
print('%r' % '948794s')
print('%d' % x)
print('/' + format(x, 'z^15,d') + '/')
print('/' + format(x, 'y^15b') + '/')
print('{0} as a new print method {1}' .format('use\'{}\'', 'is good'))

print('{0:10.2f}/{1:^15}/{2:,}/' .format(123.456, 779999, 55555))
