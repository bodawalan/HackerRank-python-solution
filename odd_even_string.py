n=int(input("Enter the number of string"))

for i in range(n):

    i=str(input("\n"))
    s1=list(i)
    lst_even=[]
    lst_odd=[]
    result=[]
    index=0
    for letter in len(s1):
        if index % 2 == 0:
            lst_even.append(letter)
        else:
            lst_odd.append(letter)
        index += 1

        s_even="".join(lst_even)
        s_odd="".join(lst_odd)
print("{} {}".format(s_odd,s_even))


for N in range(int(input())):
    S = input()
    print(S[::2], S[1::2])
for i in range(int(input())): s=input(); print(*["".join(s[::2]),"".join(s[1::2])])