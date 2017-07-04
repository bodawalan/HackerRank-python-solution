import random

class Die:
    def __init__(self,sides=2,value=0):# default side and value
        if not sides >=2:
            raise ValueError("Must have atleast two sides")
        if not isinstance(sides,int):
            raise ValueError("sides must have whole number")
        self.value=value or random.randint(1,sides)
    def __int__(self):
        return self.value

    def __eq__(self,other):
        return int(self) == other

    def __ne__(self, other):
        return int(self) != other

    def __gt__(self, other):
        return int(self) > other

    def __lt__(self,other):
        return int(self) < other

    def __ge__(self, other):
        return int(self) > other or int(self) == other

    def __le__(self, other):
        return int(self) < other or int(self) == other

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other

    def __repr__(self):
        return str(self.value)
class D6(Die):
    def __init__(self,value=0):
        super().__init__(sides=6,value=value)

class Hand(list):
    def __init__(self,size=0,die_class=None,*args,**kwargs):
        if not die_class:
            raise ValueError("you not privide the value of die class")
        super().__init__()

        for _ in range(size):
            self.append(die_class())
        self.sort()

class YourHand(Hand):
    def __init__(self,*args,**kwargs):
        super().__init__(size=5,die_class=D6,*args,**kwargs)

yh=YourHand()
print(yh)
