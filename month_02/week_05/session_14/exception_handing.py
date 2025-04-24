print('This line will print')
x=10
y=0

if x ==5:
    print("Hello")
          
print("Next line")

#print(x/y)

print('Third line')

try:
    #aldaa garch bolzoshgui
    result = 10/0
except ZeroDivisionError:
    #aldaa garval xiix uildel
    print("tegeer xuvaaj bolohgui")

print('Fourth line')



try:
    number = int(input("Too oruulna uu:"))
    result = 10/number
except ValueError:
    print("zow too oruulna uu")
except ZeroDivisionError:
    print("tegeer xuvaaj bolohgui")

print('Fifth Line')

try:
    number = int(input("Too oruulna uu:"))
    result = 10/number
except (ValueError,ZeroDivisionError):
    print("buruu orolt esvel tegeer xuvaaj oroldlogo!")


try:
    file= open ("nonexistent.txt", "r")
except Exception as e:
    print(f"Aldaa garlaa:{e}")

print("Sixth line")
try:
    x=10/0
except Exception as e:
    print(f"A;daanii torol: {type(e).__name__}")
    print(f"Aldaani messel :{str(e)}")


try:
    number = int(input("Too oruulna uu:"))
    result = 10/number
except ValueError:
    print("zow too oruulna uu")
except ZeroDivisionError:
    print("tegeer xuvaaj bolohgui")
else:
    print(f"ur dun: {result}")


# try:
#     file = open("exaple.txt", "r")
#     content = file.read()
#     print(content)
# except FileExistsError:
#     print("PAil oldoogui")
# else:
#     print(f"Pail ner: {file.name}")
#     print(f"PAil undes: {file.undest}")
# finally:
#     if 'file' in locals() and not file.closed:
#         file.close()



try:
    x = int("too bish")
except ValueError:
    print("ValueError bolovcruulj baina")
   


try:
    age=int(input("nasaa oruulna uu:"))
    if age < 0: 
        raise ValueError("nas sororg too baij bolohgui")
except ValueError as e:
    if "invalid literal" in str(e):
        print("zow too oruulna uu")
    else:
        print(e)

try:
    x=int("too bish")
except ValueError as e:
    # raise RuntimeError("Bolovsruult amjitgui bolson ") from e

 
  import traceback 

# try:
#     1/0
# except Exception:
#     traceback.print_exc()

def divide(a,b):
    try:
        int(a)
        int(b)
        result = a/b

    except ValueError:
        print("nadaa too ognu")
    except ValueError:
        print("nadaa too ognu")
    except ZeroDivisionError:
        print("too bish baina")
    except ZeroDivisionError:
        print("aldaa")
    else:
        print(result)

divide(4,0)
divide("4",5)
divide("hi","hi")