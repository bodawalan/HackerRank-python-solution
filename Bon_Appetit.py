"""n,k=input().strip().split(' ')
n,k=[int(n),int(k)]
ar=list(map(int,input().strip().split(' ')))
b=int(input().strip())"""

n=4
k=1
ar=[3,10,2,9]
b=12
if b ==((sum(ar)-ar[k])//2):
    print("exact")
else:
    print(b-((sum(ar)-ar[k])//2))


