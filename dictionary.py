"""n=int(input())
d={}
count =0
# enter the key and value in dictionary
for _ in range(n):
    k, v = input().split()
    d[k]=v"""

n = int(input())
name_numbers = [input().split() for _ in range(n)]
d = {k: v for k,v in name_numbers}
# add key for find
s_k=[]
h=0
while h< n:
    k = str(input())
    s_k.append(k)
    h +=1

# searching key and give value of that key
for k in d.keys():
    if k in s_k:
        print("{}={}".format(k,d.get(k)))
    else:
        print("Not found")



