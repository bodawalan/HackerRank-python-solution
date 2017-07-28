def cartesian_product(list1,list2):
    for i in list1:
        for v in list2:
            print((i,v),end='')


#list1=[int(input(i)) for i in range(0,2)]
list1=[int(n) for n in input().split()]
list2=[int(n) for n in input().split()]


cartesian_product(list1,list2)

"""for i in list1:
    for v in list2:
        print((i,v),end='')"""

