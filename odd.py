"""n =int(input())
if n % 2==0 and n in range(2,5):
    print("Not Weird")
elif n % 2==0 and n in range(6,20):
        print("weird2")
elif n % 2 ==0 and n >20:
        print("Not Weird1")

else:
    print("weird1")
"""

number=int(input("enter the number"))
if number % 2==0 and  (number * 4 )% 2 == 0:
    print(number ,"is even ")

else:
    print(number,"is not even")