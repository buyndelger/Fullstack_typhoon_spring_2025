class Mathuils:
    @staticmethod
    def add(x,y):
        return x+y
    @staticmethod
    def is_even(number):
        return number % 2 == 0
    


print(Mathuils.add(5,3))
print(Mathuils.is_even(4))

math = Mathuils()
print(math.add(2,3))