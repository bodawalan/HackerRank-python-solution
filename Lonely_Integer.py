"""def duplicatearray(arr):

    nosupl=[]
    for i in arr:
        if i in nosupl:
            pass

        else:
            nosupl.append(i)
    print(nosupl)
new=duplicatearray([1,2,3,4,4,5,6,3])"""


num_in=int(input("how many number of input you want?"))
num_in_list=[]
for i in range(num_in):
    num_in_list.append(int(input()))

print(num_in_list)

lonely_int=[]
unique=[]
for i in num_in_list:
    if i  in unique:
        lonely_int.append(i)
        pass
    else:
        unique.append(i)
print(lonely_int)
print(unique)
print(list(set(list(lonely_int)) ^ set(list(unique))))

