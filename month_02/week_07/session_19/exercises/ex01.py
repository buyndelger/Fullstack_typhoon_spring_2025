class Cat:
    species ="Felis catus"
    def __init__(self, name , color ,age):
        self.name = name
        self.color =color
        self.age= age * 7
    def meow(self):
        return f"MEOW! I'm a {self.name}"

    def __str__(self):
        return f"{self.name} is a {self.color} cat"
    
    def change (self , name):
        return name
    
    def __repr__(self):
        return f"Cat(name={self.name}, race={self.color})"
    
kanad =Cat("Kanad", "white" ,3)
german =Cat("German", "yellow and black" ,2)
print(f"Cat1 : {kanad.name}, {kanad.color}")
print(kanad.meow())
print(f"Cat2 : {german.name}, {german.color}")
print(german.meow())

print(kanad)
print(kanad.name)
print(kanad.color)
print(repr(kanad))

print(german)
print(german.name)
print(german.color)
print(repr(german))

print(german.species)
print(german.age)
print(german.change("Snowball"))

class book :
    def __init__(self, title, author ,pages, published_year ):
        self.title = title
        self.author = author
        self.pages = pages
        self.published_year =published_year
        