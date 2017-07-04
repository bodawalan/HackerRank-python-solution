class Person:
    def __init__(self,firstName,lastName,idNumber):
        self.firstName=firstName
        self.lastName=lastName
        self.idNumber=idNumber

    def PrintPerson(self):
        print("Name:", self.lastName + " ," ,  self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,firstName,lastName,idNumber,scores):
        super().__init__(firstName,lastName,idNumber)
        self.scores=scores

    def calculate(self):
        result= sum(self.scores)/len(scores)
        if result >= 90:
            letter = 'o'
        elif result >= 80:
            letter= 'E'
        elif result >=70:
            letter ='A'
        elif result >=55:
            letter ='P'
        elif result >=40:
            letter ='D'
        else:
            letter ='T'

        return letter

line=input().split()
firstName=line[0]
lastName=line[1]
idNum=line[2]
numScores = int(input())
scores=list(map(int,input().split()))
scores = list( map(int, input().split()) )
s = Student(firstName,lastName,idNum, scores)
s.PrintPerson()
print("Grade:", s.calculate())


"""  sample Input
    Heraldo Memelli 8135627
    2
    100 80
    
    sample output
    Name: Memelli, Heraldo
    ID: 8135627
    Grade: O
    
"""