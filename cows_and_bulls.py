import random
def cow_bull():
    list_1 = []
    cow,bull = 0,0
    v = 0
    for i in range(4):
        i = list_1.append(random.randint(0, 9))
    print(f"random guess is {list_1}")

    while True:
        num = [int(x) for x in input().split()]
        if num == list_1:
            print("you guess the right number")
            break
        elif num[v] == list_1[v]:
            print(f"you guess correct postion of {v}")
            v += 1
            cow += 1
        else:
            bull += 1




cow_bull()
