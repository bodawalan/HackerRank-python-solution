import string
import random
def id_generator(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



size=int(input("Enter the size of the password?/t"))

print(id_generator(size,))
