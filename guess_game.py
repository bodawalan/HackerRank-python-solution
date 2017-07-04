import random
def guess_game():
    guess_number = []
    random_number=random.randint(0,6)
    count = 1
    while True:

        user_input = int(input("guess the number between 1 to 5 '\t "))

        guess_number.append(user_input)
        if random_number == user_input:
            print("You sucess fully match the number")
            print(f"your guess list{guess_number}")
            print(f"you took {count}   try")
            break
        elif str(input("press Y or N for continue?")) == 'Y'.lower():
            count +=1
            continue
        else:
            print(f"random number was{random_number}")
            break

guess_game()