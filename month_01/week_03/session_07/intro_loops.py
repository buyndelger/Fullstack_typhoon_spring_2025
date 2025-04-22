fruits =["alim" ,"banana", "guzeelgen"]

print(fruits[0])
print(fruits[1])
print(fruits[2])

#1 For loop
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)
for i in range(2,8):
    print(i)
for i in range(1,10,2):
    print(i)
message="Python"

for char in message:
    print(char)

    fruits=["alim", "banana", "guzeeljegne"]
for index, fruit in enumerate(fruits):
    print(f"indexc {index}: {fruit}")


for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

for i in range(10):
    if i ==5:
        break
    print(i)

for i in range(10):
    if i%2 == 0:
        continue
    print(i)



for i in range(5):
    print(i)
else:
    print("davtalt amjiltai duuslaa!")


for i in range(5):
    if i ==3:
        break
    print(i)
else:
    print("Ene xeseg ajillahgui")


#davhar loop
for i in range(1,4):
    for j in range(1,4):
        print(f"{i} x {j} ={i*j}")
    print("------")
# ingeen davtalt 
squares=[]
for i in range(1,6):
    squares.append(i**2)
print(squares)

squares=[ i** 2 for i in range(1,6)]
print(squares)
even_squared =[i**2 for i in range(1,11) if i%2 == 0 ]
print(even_squared)