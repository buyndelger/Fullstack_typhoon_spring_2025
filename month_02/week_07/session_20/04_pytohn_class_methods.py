class Dog:
    def __init__(self, name ,breed):
        self.name= name
        self.breed =breed

    def bark(self):
    
        return f"{self.name} says WOOF!"
    def change_name(self, new_name):
        self.name= new_name


fido = Dog ("Fido", "Golden" ,"Retrever")
print(fido.bark)
fido.change_name("Buddy")
print(fido.bark())
        