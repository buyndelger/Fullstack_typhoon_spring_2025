# empty_dict = {}
# empty_dict = dict()

# student ={
#     "ner": "bat",
#     "nas": 20,
#     "xot": "Ulaanbaatar"
# }

# mixed_dict={
#     "too":42,
#     "useg":"a",
#     "jagsaalt" : [1,2,3],
#     "kortej": True,
#     "deed_toli":{"x":1,"y":2},
#     }
# person =dict(ner="Bold", nas=25, xot="Darhan")

# # items =[("alim",3)("banana",5)("jurj",2)]
# # fruits_count = dict(items)

# student={"ner": "bat", "nas":20, "xot":"Ulaanbaatar"}

# name= student["ner"]

# age=student.get("nas")
# email=student.get("email")
# email=student.get("email", "Medeelel baihgui")


# student ={"ner":"bat", "nas":20, "xot":"ULaanbaatar"}

# student["nas"] =21
# student["mergejil"]="programist"
# student.update({"nas":22, "utas":991122333, "xot":"darhan"})

# print(student)

# student={
#     "ner": "bat",
#     "nas":20,
#     "xot":"Ulaanbaatar",
#     "mergejil":"programist"
# }
# age=student.pop("nas")
# last_item=student.popitem

# del student["xot"]
# student.clear

# student={
#      "ner": "bat",
#     "nas":20,
#     "xot":"Ulaanbaatar",
# }

# age=student.keys()

# values =student.values()

# items= student.items()

# keys_list =list(student.keys())




# student={
#      "ner": "bat",
#     "nas":20,
#     "xot":"Ulaanbaatar",
# }
# for key in student:
#     print(f"{key}: {student[key]}")

# for key, value in student.items():
#     print(f"{key}:{value}")

# for key in student.keys():
#     print(key)

# for value in student.values():
#     print(values)


# original = {"a": 1 ,"b": 2 ,"c": {"x": 10 ,"y": 20 ,}}
# copy1=original.copy()
# copy2=dict(original)
# import copy
# deep_copy =copy.deepcopy(original)

# original["c"]["x"] =100
# print(copy1["c"]["x"])
# print(deep_copy["c"]["x"])

# student={
#     "ner": "bat",
#     "nas":20,
#     "xot":"Ulaanbaatar",
# }

# sorted_keys =sorted(student.keys)
# sorted.dic={k:student[k] for k in sorted_keys}
# print(sorted_dict)


# squeres= {x: x**2 for x in range(1,6)}
# print(squeres)


# even_squares ={x: x**2 for x in range(1,11)}
# print(even_squares)


# names = ["Bat", "Bold", "Caraa", "Tuya"]
# name_lengths={ name: len(name) for name in names}
# print(name_lengths)


# student={
#     "s001":{
#          "ner": "bat",
#          "nas":20,
#         "xicheeluud": ["Matematik", "Pizik" , "Programchlal"]
#     },
#     "s0002":{
#          "ner": "Bold",
#          "nas":21,
#          "xicheeluud": ["Angli hel",   "Programchlal", "Dizain"]
#     }
# }

# print(student["s001"]["ner"])
# print(student["s002"]["xicheeluud"])

# for student_id,info in students.items():
#     print(f"Suragchiin ID:{student_id}")
#     print(f"Ner:{info['ner']}")
#     print(f"Nas:{info['nas']}")
#     print(f"Xicheeluud:{','.join(info['xicheeluud'])}")
#     print()

# text="Bi chamd xairtai bi chamd xairtai gedgee xelmeer baina"
# words = text.split()
# print(words)
# word_count={}
# for word in words:
#     if word in word_count:
#         word_count[word] +=1
#     else: 
#         word_count[word] =1
# print(word_count)    

# students = [
#     { "ner": "Bat", "nas":20},
#     { "ner": "Bold", "nas":21},
#     { "ner": "Saraa", "nas":20},
#     { "ner": "Tuya", "nas":21},
# ]

# student_by_age ={}
# for student in students:
#     age =student["nas"]
#     if age in student_by_age:
#         student_by_age[age].append(student["ner"])
#     else:
#         student_by_age[age] =[student["ner"]]
# print(student_by_age)

def word_frequency(text):
    text= text.lower()
    for char in '.,?1;:()[]{}""'"":
      text =text.replace(char, "")

    words =text.split()

    frequency={}
    for word in words:
        if word in frequency:
           frequency[word] +=1
        else:
           frequency[word]=1
           
    return frequency
text ="Bi python xel surch baina. Python bol mash conirholtoi xel . Bi Python-g sain surah heregtei."
freq =word_frequency
print(freq)