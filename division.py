# expected o/p 2/3 =1 and 2/3=1.333

"""print(4/3)
print(round(4/3))



n= int(input())

for num in range (n):

    print(num * num)

y= int(input())

if y %4 == 0 and (y %100 !=0 or y % 400==0):
    print("leap year")
else:
    print("No leap year")

# if 3 o/p is 123

n= int(input())

for num in range (0,n):

    print(num+1,end='')

n, m = map(int, (input().strip().split(' ')))
arr = list(map(int, (input().strip().split(' '))))
A = set(list(map(int, (input().strip().split(' ')))))
B = set(list(map(int, (input().strip().split(' ')))))

H = 0

for i in arr:
    if i in A:
        H += 1
    if i in B:
        H -= 1

print(H)

num= int(input())
stam_list =[]
for n in range(num):
    n= str(input())
    stam_list.append(n)

v=(list(set(stam_list)))
print(len(v))

# union

num1=int(input())
num2=int(input ())
num_1=[]
num_2=[]
for n in range(num1):
    n=int(input())
    num_1.append(n)
for m in range(num2):
    m = int(input())
    num_2.append(m)

print((set(num_1)).union(set(num_2)))

Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel. 
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of  members per group where  ≠ .

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear  times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number. 
The total number of tourists or the total number of groups of families is not known to you. 
You only know the value of  and the room number list.

Input Format

The first line consists of an integer, , the size of each group.
The second line contains the unordered elements of the room number list.


Constraints


Output Format

Output the Captain's room number.

Sample Input

5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
Sample Output

8
Explanation

The list of room numbers contains 31 elements. Since k is 5, there must be 6 groups of families. In the given list, all of the numbers repeat 5 times except for room number 8. 
Hence,  8 is the Captain's room number."""
import random
total_family=input()
family_member=4* total_family
total_member=family_member +1







