def camel_case(s):

    count_camel=0
    first_case=0
    m=list(s)
    for i in range(len(m)):
        if i == 0 and m[i].islower():
            first_case += 1
        elif m[i].isupper():
            count_camel+=1

    if first_case == 1:
        return count_camel + 1
    else:

        return count_camel-1




s=str(input())
result=camel_case(s)
print(result)