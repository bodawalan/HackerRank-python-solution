import sys

def aVeryBigSum(n, ar):
    # Complete this function
    c=sum(ar)
    return c


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)


"""input
2
100001 100009

o/p
200010"""
