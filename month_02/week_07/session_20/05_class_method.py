class Dog:
    count = 0 


    def __init__(self, name ,breed):
        self.name=name
        self.breed= breed
        Dog.count +=1
        
    @classmethod
    def get_count(cls):
        return f"There are {cls.count} dogs"
    
    @classmethod
    def from_string(cls, dog_string):
        name , breed =dog_string.split("_")
        return cls(name, breed)
    


fido = Dog ("Fido", "Golden" ,"Retrever")
rex =Dog ("Rex", "German Shepherd" )


print(Dog.get_count())

buddy =Dog.from_string
print(buddy.name)
print(buddy.breed)
print(Dog.get)