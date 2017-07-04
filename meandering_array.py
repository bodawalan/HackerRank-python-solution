import copy
number=int(input("how many number do you want to input?"))
number_list=[]
for i in range(number):
    array=int(input())
    number_list.append(array)

print(number_list)
# empty array for adding value in list
tmp=[]
i=0

m=len(number_list)
while i<m:
    # when last element left in array it will add on our tmp list
    if i >= len(number_list):
        tmp.extend(number_list)
        # once all value add in array it will break the program
        if len(tmp) == m:
            break
    else:
        high=max(number_list)
        low=min(number_list)


        tmp.append(high)
        tmp.append(low)
        #number_list.remove(high)
        #number_list.remove(low)
# remove the element after added in the list
        number_list.remove(high)
        number_list.remove(low)
        #print(len(number_list))
        #print(tmp)


    i +=1


print(tmp)

