import sys
n= int(input())
k=bin(n)[2:]
a=max(k.split('0')).count('1')


print(a)