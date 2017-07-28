from itertools import permutations,combinations



s1,n = input().split()
for i in range(1,int(n)+1):

       print(*[''.join(i) for i in combinations(sorted(s1),i)],sep='\n')