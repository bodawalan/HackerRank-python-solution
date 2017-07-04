import sys
n=int(input().strip())

arr=[int(arr_tmp) for arr_tmp in input().strip().split(' ') ]
print(" ".join(str(x) for x in arr[::-1]))
