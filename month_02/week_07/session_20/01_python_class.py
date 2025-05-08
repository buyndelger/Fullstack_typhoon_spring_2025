class Dog:
    species ="Canis familiaris"

    def __init__(self , name,breed):
        self.name = name
        self.breed = breed



fido = Dog ("Fido", "Golden" ,"Retrever")
rex =Dog ("Rex", "German Shepherd" )

print(Dog.species)
print(fido.species)
print(rex.species)



Dog.species= "Canis lupus familiaris"
print(fido.species)
print(rex.species)

fido.species= "Changed for Fido"
print(fido.species)
print(rex.species)

