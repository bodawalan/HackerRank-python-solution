def duplicatearray(arr):

    nosupl=[]
    for i in arr:
        if i in nosupl:
            pass

        else:
            nosupl.append(i)
    print(nosupl)

def duplicate_set(arr):

    dup=(set(arr))
    print(dup)




new=duplicatearray([1,2,3,4,4,5,6,3])
other=duplicate_set(arr=[1,2,3,4,4,5,6,3])