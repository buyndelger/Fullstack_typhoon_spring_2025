def caesar_cipher(текст, шилжүүлэх_тоо,  үйлдэл):
    result = ""
    if үйлдэл == "esreg":
      шилжүүлэх_тоо = -шилжүүлэх_тоо
    for char in текст:
        if char.isupper():
            start = ord("A")
            result += chr((ord(char) - start + шилжүүлэх_тоо) % 26 + start)
        elif char.islower():
            start = ord("a")
            result += chr((ord(char) -start + шилжүүлэх_тоо) % 26 + start)
        elif char.isdigit():
            start = ord("0")  
            result += chr((ord(char) -start  + шилжүүлэх_тоо) % 10 + start)
        else:  
            result += char
    return result

while True:
    үйлдэл= input("ireg эсвэл esreg: ").lower()
    текст = input("Текст: ")
    шилжүүлэх_тоо= int(input("Шилжүүлэх тоо: "))
    print("Үр дүн:", caesar_cipher(текст, шилжүүлэх_тоо, үйлдэл))
    if input("Дахин хийх үү? (yes/no): ").lower() != "yes":
        break
