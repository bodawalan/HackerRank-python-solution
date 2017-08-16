import sys

def birthdayCakeCandles(n, ar):
    # Complete this function

    cake=[]
    for i in ar:
        if i == max(ar):
            cake.append(i)
    return len(cake)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
