
"""n=int(input())
print(n*(n-1)for _ in range(n))"""


def factorial(n):
    fact =1
    for i in range(1,n+1):
        fact=fact * i
    print(fact)




factorial(n=int(input()))
