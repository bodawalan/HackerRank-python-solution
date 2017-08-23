"""
Generate the integers from 1 to 10 in a list. Square all the even numbers. Do this using a list
comprehension.
"""

"""l=list(range(1,10))
print(l)
l1=[]
for i in l:
    if i % 2 == 0:
        l2=i *i
        l1.append(l2)

print(l1)"""

print([i*i for i in range(1,11) if i % 2== 0])

