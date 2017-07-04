class Person:
    def __init__(self,initialAge):
        self.age=0
        self.initialAge = initialAge
        if initialAge < 0:
            self.age=initialAge
            print('Age is not valid, setting age to 0.')
        else:
            self.age = initialAge


    def amIold(self):
        if self.initialAge < 13:
            print("you are young")
        elif self.initialAge >= 13 and self.initialAge < 18:
                print("You are a teeneger.")
        else:
            print("you are old")


    def yearpasses(self):
        self.initialAge +=1


t=int(input("how many input you want?"))
for i in range(0,t):
    age=int(input("Enter the age:"))
    p=Person(age)
    p.amIold()
    for j in range(0, 3):
        p.yearpasses()
    p.amIold()
    print(" ")

