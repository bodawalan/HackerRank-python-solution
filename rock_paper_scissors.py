

def game(pl_1,pl_2):
    print(pl_1,pl_2)

    if pl_1==pl_2:
        print("try once again")
    elif pl_1== 'A':
        if pl_2=='C':
            print("pl_1 win")
        else:
            print("pl_2 is win")
    elif pl_1 =='C':
        if pl_2 =='B':
            print("pl_1 is win")
        else:
            print("pl_2 is win")
    elif pl_1 == 'B':
        if pl_2 == 'A':
            print("pl_1 is win")
        else:
            print("pl_2 is win")
    else:
        print("wrong choice")

print("Enter choice A=rock"
             "B=paper,"
             "c=scissors"
             )
A,B,C="rock","paper","scissors"
pl_1=str(input("player one enter your choice "))
pl_2=str(input("player two enetr your choice "))

game(pl_1,pl_2)
