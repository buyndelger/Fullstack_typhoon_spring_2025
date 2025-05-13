class Animal:
    def __init__(self, name):
        self.name=name
        

    def speak(self):
        pass
dinosaur= Animal("Dino")
print(dinosaur.name)
dinosaur.speak()


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
    

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    

nogoon =Dog("nogoonoo")
banhar=Cat("banhar")

print(banhar.speak())
print(nogoon.speak())

class Human:
    