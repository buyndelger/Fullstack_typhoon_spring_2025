def create_point(x,y):
    return (x,y)
def calculate_distance( point1, point2):
    import math
    return math.sqrt((point2[0] - point1[0])**2+(point2[1] - point1[1]))

set1 ={1,2,3,4,5}


set2={1,2,3,4,5}
print(set2)

set3=set([1,2,3,4,5])

empty_set=set()

letters =set("hello")
print(letters)

fruits={"alim","banana", "jurj"}


fruits.add('usan uzem')
print(fruits)

fruits.update(["mango", "kiwe"])
print(fruits)
fruits.remove("banana")
print(fruits)

fruits.discard("liir")


popped =fruits.pop()
print(popped)
print(fruits)

fruits.clear()
print(fruits)
A={1,2,3,4,5}
B={4,5,6,7,8}
print(A|B)
print(A.union(B))


print(A&B)
print(A.intersection(B))


print(A-B)
print(A.difference(B))

print(A^B)
print(A.symmetric_difference(B))


A={1,2,3,4,5}
B={1,2,3}
C={6,7,8}

print(B.issubset(A))
print(A.issuperset(B))

print(A.isdisjoint(C))
D={1,2,3,4,5}
print(A==D)


numbers = [1,2,2,3,4,4,5]
unique_numbers=list(set(numbers))
print(unique_numbers)


fruit={"alim","banana","jurj"}
print("alim" in fruits)

text1="hello"
text2="world"
common_letters= set(text1)& set(text2)
print(common_letters)

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
common_elements = list(set(list1) & set(list2))
print(common_elements)

frozen=frozenset([1,2,3,4,5])

A= frozenset([1,2,3,4,5])
B=frozenset([4,5,6,7,8])
print(A|B)

data ={frozen:"Frozen set tulhuur"}
print(data[frozen])
def count_unique_words(text):
    words =text.lower().split()
    unique_words=set(words)
    print(words)
    print(unique_words)
    return len(unique_words)


text="Bi Python hel surcg baina. Python bol mash conirholtoi hel."
print(f"davtagdashgui ugciin too:{count_unique_words(text)}")