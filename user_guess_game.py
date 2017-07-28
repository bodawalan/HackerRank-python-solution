""" 
#first user guess the number
# system divides the number in 3 equal rannge and guess the numbers
ess the number between the user guess range using random
#if number high user say high 
# 
"""
import random
a=0
b=10
while True:

    system_guess=random.randint(a,b)
    print(system_guess)
    user_input=str(input(

    """This number is higher than your number press H
    This number is lower than your Guess Number L
    This number is exact match say Y"""
                ))


    if user_input == 'Y':
        print("Thanks to guess number")
        break
    elif user_input == 'H':
        a=0
        b=system_guess
    elif user_input =='L':
        b=10
        a=system_guess