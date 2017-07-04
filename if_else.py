"""print("hello")
n= 18
if n % 2 == 0:
    if 3<= n <=6:
        print("weirdl1")
    elif 6<= n <= 20:
        print ("not weird")
    elif n >20:
        print("weirdl")
else:
    print ("odd")

n = int(input())
integer_list = map(int, input().split())
t=(n,integer_list)
print(hash(t))

find second largest element"""



n = int(input())
arr = map(int, input().split())
i=0


while(arr[i]  == arr[i+1]):
    i =i+1
print(arr[i+1])


