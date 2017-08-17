birds=[1,4,4,4,5,3,3,3,5,5,5]
types=0
new_bird=[]
sorted_birds=birds[::-1]
count=0
for i in range(len(sorted_birds)):
    if count == 0:
        types=sorted_birds[i]
        count =1
    else:
        if (types==sorted_birds[i]):
            count += 1
        else:
            count -=1
print(types)

