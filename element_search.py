"""Write a function that takes an ordered list of numbers
(a list where the elements are in order from smallest to largest) and another number.
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean."""

user_list=[int(x) for x in input().split()]
print(sorted(user_list))
new_user=int(input("Enter the number you want to search in the list/t"))
def ele_search():
    return  new_user in user_list
print(ele_search())