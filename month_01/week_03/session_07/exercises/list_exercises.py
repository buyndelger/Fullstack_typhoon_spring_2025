#exerises-1
Hool=['цуйван', 'хуушуур', 'будаатай хуурга', 'пицца', 'тахианы шөл']
print(Hool[0])
print(Hool[-1])
print(Hool[2])
#exercises-2
numbers= [100, 200, 300, 400, 500]
print(numbers)
numbers[2]=999
print(numbers)
numbers.append(600)
print(numbers)
numbers.insert(0, 50)
print(numbers)
numbers.remove(50)
print(numbers)
#exerisee-3
jagsaalt= [1,2,3,6,5,4]
print(jagsaalt)
jagsaalt.sort()
print(jagsaalt)
jagsaalt.reverse()
print(jagsaalt)
jagsaalt_copy =jagsaalt[:]
print(jagsaalt)
print(len(jagsaalt))
#exercises-4
too =[0,1,2,3,4,5,6,7,8,9]
print(too)
print(too[0:3])
print(too[7:])
print(too[2:7])
print(too[1:10:2])
#exericses-5
jims= ['алим', 'банана', 'гүзээлзгэнэ', 'усан үзэм', 'киви']
for jimse in jims:
    print(jimse)
for index, jimse in enumerate(jims):
    print(f"{index}: {jimse}")


#exercises-6
too = [1,2,3,4,5,6,7,8,9,10]
print(too)
print(too[1:10:2])
squares=[]
for too in range (1,11):
    squares.append(too ** 2)
print(squares)
even_squares = [too **2 for too in range (6,11) if too]
print(even_squares)





