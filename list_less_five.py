number=int(input("enter the number of input you wnat to enter\t"))
list1=[]
less_five_list=[]
for i in range(number):
    i = int(input())
    list1.append(i)

for i in list1:
    if i <=5:
        less_five_list.append(i)
print(less_five_list)
