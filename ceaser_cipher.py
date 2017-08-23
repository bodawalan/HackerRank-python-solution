def ceaser_cipher(s,k):

    for i in s:
        a = 65 if i.isupper() else 97
        print((chr(a + (ord(i) - a + k) % 26)) if i.isupper() or i.islower() else i, end='')

s=str(input())
k=int(input())
result=ceaser_cipher(s,k)
print(result)

