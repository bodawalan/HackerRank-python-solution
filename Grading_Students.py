import sys


#grades=[37,45,66]
    # Complete this function
def solve(grades):
    list_grade=[]
    for i in grades:
        if i <= 37:
            list_grade.append(i)
        elif i > 37 and (i %5== 0):
            list_grade.append(i)
        elif  i > 37:
            l=i + 1
            l1=l+1
            l2=l1+1
            print ("i am ",l)

            if (l%5==0):
                list_grade.append(l)
            elif(l1%5==0):
                list_grade.append(l1)
            elif l1 == 40:
                list_grade.append(l1)
            else:
                list_grade.append(i)
    return list_grade






#print(list_grade)





n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
#print("\n".join(map(str, result)))
print(result)