class Dog:


    pass

banhar = Dog()
print(banhar)
bullddog = Dog()
print(bullddog)


class Cat:
    def __init__(self, name , race):
        self.name = name
        self.race =race
    def meow(self):
        return f"MEOW! I'm a {self.name}"

    def __str__(self):
        return f"{self.name} ni {self.race}"
    
    def __repr__(self):
        return f"Cat(name={self.name}, race={self.race})"



koshka =Cat("koshka" ,"Marine Coon")
print(koshka)
print(koshka.meow())
print(koshka.name)
print(repr(koshka))
ireenee =Cat("ireenee" , "Mongolia")
print(ireenee.race)
print(ireenee.meow())
print(repr(ireenee))





class Horse:
    species = "Canis faliliaris"

    def __init__(self, name , age):
        self.name =name
        self.age =age

black_horse =Horse("Har Mori" , 3)
print(black_horse)
print(black_horse.age)
print(black_horse.name)


class Dog:
    def __init__(self,name, age):
        self.name=name
        self.age=age

    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def bark(self, sound):
        return f"{self.name} says {sound}"
    

balt =Dog(name="Balt", age=5)
burged =Dog(name="Burged", age=2)
print(balt.description)
print(balt.bark("GAV GAV"))

print(burged.description)
print(burged.bark("hav hav"))


class BankAccount:
    def __init__(self , owner,balance=0):
        self.owner = owner
        self._balance = balance
        self._account_number = "123456"

    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negativ")
        self._balance =value

buyndelger_account = BankAccount(10000)
print(buyndelger_account)



class Dog:
    tricks =[]

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self , trick):
        self.tricks.append(trick)


d =Dog("fido")
e =Dog("BUDDY")
d.add_trick("roll over")
e.add_trick("play dead")
print(d.tricks)
print(e.tricks)