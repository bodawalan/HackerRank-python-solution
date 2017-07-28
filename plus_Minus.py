import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
c1=0
c2=0
c3=0
for num in arr:
    if num>0:
        c1 += 1
    elif num <0:
        c2 += 1
    elif num == 0:
        c3 += 1

print(c1/len(arr))
print(c2/len(arr))
print(c3/len(arr))
