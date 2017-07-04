number = int(input("up to how many word you want Enter"))
li_st = []
for st_r in range(number):
    st_r = str(input("Enter the word:"))
    start = -1
    for i in range(0, len(st_r) - 1):
        if st_r[i] < st_r[i + 1]:
            start = i
    if start == -1:
        print("No answer")
        continue

    end = -1
    for j in range(start + 1, len(st_r)):
        if st_r[start] < st_r[j]:
            end = j
    st_r[start] = (st_r[end])
    st_r[end] = st_r[start]
    a = st_r[start + 1:]
    a.sort()

    for j in range(start + 1, len(st_r)):
        st_r[j] = a[j - start - 1]
    print("".join(st_r))
