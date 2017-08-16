def  oddNumbers(l, r):

    for i in range(l,r+1):
        if i % 2 != 0:
            return i

w=oddNumbers(2,5)
print(w)