"""birth_dict={"Nishit":"13,'March'","zalak":"2nd january"}

print(f"we know the birth day of {birth_dict}")

user_input=str(input("Enter the name whose birt date you looking for?"))
print(birth_dict.get(user_input))"""
d = dict(input().split() for _ in range(3))
user_input=str(input("Enter the name whose birt date you looking for?"))
print(d.get(user_input))