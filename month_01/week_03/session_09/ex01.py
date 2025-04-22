for i in range(10):
    print('Hello world')
    print('############')
for i in range(10):
    print('Hello world')
    print('############')



def greeting(name):
     for i in range(2):
       print(f'Hello {name}')



greeting('tamir')
greeting('balt')
greeting('ouynbold')
greeting('hangai')

#olon parametrteu punkts
def add (a,b):
    """  Hoer toog nemeh .
    
    Args:
    a (ing/float):Ehnii too
    b(int?float): Xoer dahi too
    
    Returns:
    int/float :Xoer toonii niilber
    """

    return a+b


result = add(5,3)
print(result)

def addThree(a,b,c):

    return a+b+c
result = addThree(2,5,7)
print(result)


def multiply(a,b):
    return a * b


result = multiply(5*6)
print(result)