class Animal:
    def __init__(self, name ,age):
        self.name =name
        self.age = age

    def info(self):
        return f"{self.name} is {self.age} years old"

class Dog(Animal):
    def __init__(self, name, age ,breed):
        super().__init__(name, age)
        self.breed = breed

    def info(self):
        basic_info =super().info()
        return f"{basic_info} and is a{self.breed}"
    

rex=Dog("Rex" , 3, "German Sherherd")
print(rex.info())
print(isinstance(rex.Dog))
print(isinstance(rex, Animal))
print(isinstance(Dog, Animal))

#exercise
class Rectangle(Shape):
    def __init__(self, widht, height):
        self.widht =widht
        self.height = height

    def area(self):
        

class Shape:
    def area(self):
        pass


    def perimeter(self):
