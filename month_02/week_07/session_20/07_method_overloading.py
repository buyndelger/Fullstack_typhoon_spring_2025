class Calculator:
    def add( self, *args):
        return sum(args)
    def multiplay(self , x, y=1,z=1):
        return x*y*z
    

calc = Calculator()
print(calc.add(1,2))
print(calc.add(1,2,3,4))
print(calc.multiplay(5))
print(calc.multiplay(5,2))
print(calc.multiplay(5,2,3))