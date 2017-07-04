class NumString:
    def __init__(self,value):
        self.value=str(value)
    def __str__(self):
        print( self.value)
    def __int__(self):
        print( int(self.value))
    def __float__(self):
        print( float(self.value))


five=NumString(5)
print(str(int))