s = 'hello'
print(s)
s(0)="H" +s[1:]
print(s)
s1= "hello"
s2=s1.upper()
print(s1)
print(s2)

id_before =id(s1)
s1 =s1 +"world"
id_after = id(s1)
print(id_before== id_after)
