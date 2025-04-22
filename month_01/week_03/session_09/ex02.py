def profile(name, age):
    print(f"{name} ni {age} nastai")

profile("Bold", 25)



profile( age=25, name="bold" )


def profile(name,age=30, city="Ulaanbaatar"):
    print(f"{name} ni {age} nastai, {city} d amdirdag")


profile("Bold")
profile("Caraa" ,25)
profile("Bayr" ,city="darhan")

def sum (*numbers):
    """duriin toonii argumentiin niilber olox,

    Args:
    *numbers: Xuvisah toonii argument
    Returns:
    int/float Ogogdol toooniii niilber
    """

    total =0
    for number in numbers:
        total += number
    return total

print(sum(1,2,3))
