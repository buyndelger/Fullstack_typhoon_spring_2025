name ="John"
age =25
height =1.75
is_student =True
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

x=y=z=0
print(x,y,z)

a,b,c=1,2,3
print(a,b,c)
coordinates=(3,4)
x,y=coordinates
print(x,y)
a,b =5,10
a,b=b,a
print(a,b)
x=10
print(type(x))

float_number =float(10)
integer = int (3.14)
string_number =str(42)

print(type(float_number))
print(type(integer))
print(type(string_number))


is_active=True
is_completed=False


print(False and False)
print(False or True)
print(True or False)
print(True or True)



print(False or False)
print(True or False)
print(False or True)
print(True or True)

print(not False)
print(not True)


print(True and False)
print(True or False)


fruits = ["alim" "banana" "intoor"]
mixed_list =[1, "sain baina", 3,14,True]

first_fruit =fruits[0]
last_fruit =fruits[-1]


fruits.append("ulaan looli")
fruits.insert(1, "mango")
fruits.remove("banana")
popped_fruit =fruits.pop()

numbers =[0,1,2,3,4,5]
subset =numbers[1:4]



numbers =range(5)
print(numbers)
numbers =range(2,7)
print(numbers)
even_numbers=range (0,10,2)
numbers_list=list(range(5))
print(numbers_list)
  

x=10

x +=5 #x=x+3(15)
x -=3   #x=x-3(12)
x *=2  #x=x*2(24)
x/=4    #x=x**4(6.0)
x //=2  #x=x//2(3.0)
x %=2   #x=x%2(1.0)
x**=3   #x=x**3(1.0)


a,b,c=1,2,3

a=10
b=5
equal =a==b
not_equal =a !=b
greater_than =a>b
less_than =a<b
greater_equal = a>=b
less_equal =a<=b
result =1<3<5
result=5>3<1