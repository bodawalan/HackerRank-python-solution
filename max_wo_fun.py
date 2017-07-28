user_list=[int (x) for x in input().split()]
j=user_list[0]
for i in user_list:

    if  j < i:
        j=i

print(j)


