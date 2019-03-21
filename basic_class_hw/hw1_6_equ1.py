import math
print("aX^2+bx+c=0")
a = int(input("input a\n"))
b = int(input("input b\n"))
c = int(input("input c\n"))
s1 = b*b-4*a*c
if s1 > 0 :
    print("2roots root1: %f\t root2: %f" % ((math.sqrt(s1)-b)/2*a, (-math.sqrt(s1)-b)/2*a))
elif s1 == 0 :
    print("1 root: %f\t" % (-b/2*a))
else:
    print("not 實數根")
