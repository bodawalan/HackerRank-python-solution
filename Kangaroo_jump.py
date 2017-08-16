


import sys

def kangaroo(x1, v1, x2, v2):
    """jump=x1+v1
    jump_2=x2+v2
    result=[]
    while jump < 100000 and jump_2 < 100000:
        if jump==jump_2:
            
            result.append('YES')
            break
        else:

            result.append('NO')

        jump +=v1
        jump_2+=v2

    return 'YES' if 'YES' in result else 'NO'"""
    if v1 > v2 and (x2-x1)%(v1-v2) == 0:
        print ("YES")
    else:
        print ("NO")

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)

# https://www.hackerrank.com/challenges/kangaroo