# import math
import random
pk = []
pk_patter = ['a', 'b', 'c', 'd']
# build poker
for i in range(13):
    for j in range(4):
        pk.append('%s_%d' % (pk_patter[j], (i+1)))
# print(pk)
random.shuffle(pk)
p1 = pk[0:0+13]
p2 = pk[13:13+13]
p3 = pk[13*2:13*2+13]
p4 = pk[13*3:13*3+13]
print(p1)
print(p2)
print(p3)
print(p4)
