fruits = ["алим", "банана", "гүзээлзгэнэ"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "хоёр", 3.0, True]
empty_list = []

print(type(fruits))
print(fruits)

#ereg 
print(fruits[0])
print(fruits[1])
print(fruits[2])
#sorog
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

#Element oorchloh
fruits[0] = "үзэм"
print(fruits) 
# Nemeh
fruits.append("киви")
print(fruits) 
# todorhoi bairlald oruulah
fruits.insert(1, "манго")
print(fruits) 
#buh element ustgah

fruits.remove("банана")
print(fruits)

removed_fruit =fruits.pop(1)
print(removed_fruit)
print(fruits)

fruits.clear()
print(fruits)

fruits = ["алим", "банана", "гүзээлзгэнэ"]

#jagsaaltiiin urt
print(len(fruits))

#eremlex
fruits.sort()
print(fruits)
#urvuu eremblex
fruits.reverse()
print(fruits)
# Жагсаалтыг урвуу эрэмбэлэх

# Элементийн индексийг олох
print(fruits.index("банана")) 
# Элементийн тоог тоолох
print(fruits.count("банана")) 
fruits_copy =fruits.copy()
print(fruits_copy)
more_fruits = ["kiwi", "mango"]
fruits.extend(more_fruits)
print(fruits)


numbers = [0,1,2,3,4,5,6,7,8,9]
print(numbers[2:5])

print(numbers[:5])

print(numbers[5:])
print(numbers[1:9:2])
numbers_copy=numbers[:]
print(numbers_copy)

