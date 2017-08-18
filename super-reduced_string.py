s="abccddd"

j = 0
count = 0
new_count = 0
for i in range(len(s)):
    print(i)
    if (count == 0):
        j = s[i]
        count = 1
    else:
        if (j == s[i]):
            count = 0
            new_count += 1
        else:
            j += 1
print(new_count)