"""Lily has a chocolate bar consisting of
a row of  n squares where each square has an integer written on it.
She wants to share it with Ron for his birthday, which falls on month   m and day .
Lily wants to give Ron a piece of chocolate only if it contains m consecutive squares whose integers sum to d.

Given m,d , and the sequence of integers written on each square of
Lily's chocolate bar, how many different ways can Lily break off a ' \
piece of chocolate to give to Ron?

For example, if m=2 ,d=3  and the chocolate bar contains 
rows of squares with the integers  written on them from left to right,
the following diagram shows two ways to break off a piece:"""

#https://www.hackerrank.com/challenges/the-birthday-bar


import sys

def solve(n, s, d, m):

    tp = (len(s) - m) + 1  # total number of pieces possible
    return len([1 for i in range(tp) if sum(s[i:i + m]) == d])



n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
