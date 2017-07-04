def palidrome(str):
    if str ==str[::-1]:
         return True;
    else :
        return False;

print(palidrome("N"))


def main():
    inputStr = input("Enter a string":")
    if isPalindrome(inputStr):
        print ("String is Palindrome")
    else:
        print("String is not palindrome")


def isPalindrome(string):
    if len(string) <= 1:
        return True
    if String[0] == String[len(string) - 1]:
        return isPalindrome(string[1: len(string) - 1])
    else:
        return False

