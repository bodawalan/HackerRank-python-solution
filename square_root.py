#a=[2,3,4,5,6,7,8,9]
from math import *
import collections
def getmin(a):
   a_1=[]
   for i in a:
      a=float(ceil(sqrt(i)))
      a_1.append(a)



   b=[item for item, count in collections.Counter(a_1).items() if count > 1]
   return len(b)+1

a, b = map(int, input().split())


#print(list(range(a,b)))
o_p=getmin(list(range(a,b)))
print(o_p)