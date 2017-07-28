from collections import Counter

N = [1,2,2,2,1,1,2,2,2,3,4]
C = Counter(N)

count = max(C.values())
print(count)

print([ [k,]*v for k,v in C.items()])