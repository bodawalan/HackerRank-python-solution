

"""Item​ ​1
Write a function that inputs a list and removes any empty lists inside it, then returns the result.
It should also remove any nested empty lists."""

"""number=int(input())
print(range(number))
lis=[]
for i in range(number):

    a=[int(x) for x in input().split()]
    lis.append(a)
for i in lis:
    if len(i)==0:
        lis.remove(i)
print(lis)"""

l=[[1,2,3],[4,5,6],[[1,3,4]],[]]
for i in l:
    if len(i)==0:
        l.remove(i)
print(l)

