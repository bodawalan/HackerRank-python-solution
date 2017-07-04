# Q.1
#
# Write a function that takes as input a minimum and maximum integer and returns
# all multiples of 3 between those integers.  For instance, if min=0 and max=9,
# the program should return (0, 3, 6, 9)
#
# A

# you can type here

def func(min, max):
    for in xrange(min, max):
        if (i % 3 == 0)
            print
        i
    end


# Q.2
# Write a function to detect whether a string is a palindrome - that is,
# the string reads the same in reverse as it does forward. Samples:
# racecar, tacocat, madam, level, etc.  Function should return True or False



def main():
    inputStr = input("Enter a string": ")
    if ispalindrome(inputStr):
        print("String is Palindrome")
    else:
        print("String is not palindrome")


def isPalindrome(string):
    if len(string) <= 1:
        return True
    if String[0] == String[len(string) - 1]:
        return isPalindrome(string[1: len(string) - 1])
    else:
        return False


# Q.3

# Modify your function to work with sentences, ignoring punctuation and capitalization.
# For instance, these should be detected as palindromes:
#
# Eva, Can I Stab Bats In A Cave?
# A Man, A Plan, A Canal-Panama!

import string


def isPalindrome
    whitelist = set(string.ascii_lowercase)


s = s.lower
s = ''.join(([char for char in s if char in whitelist])
return s = s[::-1]

revstring = mystring[::-1]

if (mysrtring == revstring):
    print("its a palindrome")
else:

# Q.4

# if tuples are immutable, why does this work?

mytuple = (1, 2, 'abc', ['x', 'y'])
mytuple[3].append('z')
mytuple
# (1, 2, 'abc', ['x', 'y', 'z'])

# But this does not work?

mytuple[3] = ['x', 'y', 'z']

#    Traceback (most recent call last):
#      File "<stdin>", line 1, in <module>
#    TypeError: 'tuple' object does not support item assignment

# Q.5

# Write a function to find the longest number of consecutive appearances of a
# character in a string
#     for example: 'fzccsawetaaafb' => (a, 3)


word = "foo"
count = 1
lenght = ""
for i in range(1, len(word)):  # range(1, 3)
    if word[i - 1] == word[i]:  # word[3] <-- key error
        count += 1
else:
    length += word[i - 1] + "repeats +str(count)+", "
    count = 1
length += ("and" + word[i] + "repeats" + str(count))
print(length)
b

"aabbbbbbccaaa"

("b", 6) < - output

if (cur_count > count)
    count = cur_count;
    res = str


# Q.6

# Write a function to swap the elements of one list with another, for examples:
#
# l1 = [1,2,3]
# l2 = ['a', 'b', 'c']
# swap_elements(l1, l2)
#
# l1 is now ['a', 'b', 'c']
# l2 is now [1,2,3]

def swap_elements(11, 12)
    11, 12 = 12, 11

# Jon - output here:

>> > def swap_elements(l1, l2):
    ...
    l1, l2 = l2, l1


...
>> > l1 = [1, 2, 3]
>> > l2 = ['a', 'b', 'c']
>> >
>> > swap_elements(l1, l2)
>> > l1
[1, 2, 3]
>> > l2
['a', 'b', 'c']

import dis


def swap1():



