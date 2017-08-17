#s=[100,8 ,49 78 36 25 96 10 67 78 58 98 8 53 1 4 7 29 6 59 93 74 3 67 47 12 85 84 40 81 85 89 70 33 66 6 9 13 67 75 42 24 73 49 28 25 5 86 53 10 44 45 35 47 11 81 10 47 16 49 79 52 89 100 36 6 57 96 18 23 71 11 99 95 12 78 19 16 64 23 77 7 19 11 5 81 43 14 27 11 63 57 62 3 56 50 9 13 45]
from collections import Counter

44 55 11 15 4 72 26 91 80 14 43 78 70 75 36 83 78 91 17 17 54 65 60 21 58 98 87 45 75 97 81 18 51 43 84 54 66 10 44 45 23 38 22 44 65 9 78 42 100 94 58 5 11 69 26 20 19 64 64 93 60 96 10 10 39 94 15 4 3 10 1 77 48 74 20 12 83 97 5 82 43 15 86 5 35 63 24 53 27 87 45 38 34 7 48 24 100 14 80 54

n = int(input())
socks = Counter(input().split())
print(sum(map(lambda x: x // 2, socks.values())))
s=[1,2,3,4,4,4,3,3,3,6,6,6,6,6,12,13,14,15,16,12,14,100,100,49,49,23,45,23,12,43,49]

s_sorted=sorted(s)
print(s_sorted)
j=0
count=0
new_count=0
for i in range(len(s_sorted)):
    print(i)
    if (count == 0):
        j=s_sorted[i]
        count = 1
    else:
        if (j == s_sorted[i]):
            count = 0
            new_count +=1
        else:
            j += 1

print(new_count)
"""types=0
count=0
for i in range(len(s)):
    if (count == 0):
        types=s[i]
        count = 1
    else:
        if (types == s[i]):
            count += 1
        else:
            count -= 1"""


