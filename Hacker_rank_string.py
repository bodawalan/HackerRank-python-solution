def isSubSequence(str1, str2, m, n):
    j = 0  # Index of str1
    i = 0  # Index of str2

    # Traverse both str1 and str2
    # Compare current character of str2 with
    # first unmatched character of str1
    # If matched, then move ahead in str1

    while j < m and i < n:
        if str1[j] == str2[i]:
            j = j + 1
        i = i + 1

    # If all characters of str1 matched, then j is equal to m
    return j == m


# Driver Program

str1 = "hackerrank"
str2 = "hackerhjddrank"
m = len(str1)
n = len(str2)

print(
"Yes" if isSubSequence(str1, str2, m, n) else "No")