def prime_number():
    return int(input("Enter the number for check is prime or not? '/t"))

number=prime_number()
if number >1:
    for i in range(2,number):
        if number % i==0:
            print(f"this {number} is not prime")
        else:
            print(f"This {number} is prime")
else:
    print(f"This {number}is not prime")