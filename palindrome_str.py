# Q.1
# Write a function to detect whether a string is a palindrome - that is,
# the string reads the same in reverse as it does forward. Samples:
# racecar, tacocat, madam, level, etc.  Function should return True or False


"""def palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

print(palindrome(input("enter the string: \t")))"""

# Q.3

# Modify your function to work with sentences, ignoring punctuation and capitalization.
# For instance, these should be detected as palindromes:
#
# Eva, Can I Stab Bats In A Cave?
# A Man, A Plan, A Canal-Panama!


import string

def palindrome_str(STR_1):
    STR_1=list(filter(str.isalnum,STR_1.upper()))#create list and removing punctuation
    if STR_1==STR_1[::-1]:
        return True
    else:
        return False

print(palindrome_str(str(input("enter the string"))))