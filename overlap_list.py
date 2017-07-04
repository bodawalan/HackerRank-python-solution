"""l1=set([1,2,3,4,5])
l2=set([3,4,5,6,7,8,9])
l3=[]
for i in l1:
    for y in l2:
        if i ==y:
            l3.append(i)

print(l3)"""
l2=[1,2,3,4,5,6,7]

l1=[ i  for i in l2 if i %2==0]
print(l1)