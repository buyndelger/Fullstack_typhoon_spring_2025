#dasgal-1
i =1
while i<11:
    print(i)
    i+=1
print('======')
    #dasgal-2
for i in range(2,21,2):
    print(i)
    #dasgal-3
ners =['Болд','Сараа','Дорж','Нара']
for ner in ners:
    print(ner)
    #dasgal-4
for i in range(1,21):
    if i % 7==0:
        print(f"7d xuvaagdag ehnii too{i}")
        i+=1
        break
        


    #dasgal-5
for i in range(21):
    if i %3==0:
          continue
    print(i)
    #daslgal-6
for i in range(1,6):
    for j in range(1,6):
        print(f"{i} x {j} ={i*j}")
    #daslgal-7

# else:
#     for i in range[2,]:
        
            # print("7 анхны тоо мөн эсэх: True")
    #dasgal-8
squares=[]
for i in range(1,6):
    squares.append(i**2)
print(squares)


#daslgal-9
jims =["алим", "алим","гүзээлзгэнэ"]
for index, fruit in enumerate(jims):
  print(f"Индекс {index}: {fruit}")
#dasgal-10
xvn= {
 "нэр": "Болд",
 "нас": 30,
 "хот": "Улаанбаатар"
}
for key, value in xvn.items():
    print(f"{key}: {value}")
