"""
Exception Handling - Дасгал ажлууд.

Энэ файл нь Python exception handling-н талаар сурахад туслах дасгалуудыг агуулна.
"""

# ===============================================================
# Дасгал 1: Үндсэн Exception Handling
# ===============================================================


def exercise_1():
    
    """
    Try-except блокыг ашиглан ZeroDivisionError алдааг барих.

    Даалгавар:
    1. Хэрэглэгчээс тоо аваад 10-г тэр тоонд хуваах
    2. Хэрэв хэрэглэгч 0 оруулбал алдааг барьж, зохих мессеж харуулах
    """
    # Энд кодоо бичнэ үү
    try:
        number = int(input("Too oruurlna uu:"))
        result = 10 / number
    except ZeroDivisionError:
        print("Тэгээр хуваах боломжгүй!")
exercise_1()


# ===============================================================
# Дасгал 2: Олон төрлийн алдааг барих
# ===============================================================


def exercise_2():
    """
    Олон төрлийн алдааг барих.

    Даалгавар:
    1. Хэрэглэгчээс тоо аваад, түүнийг квадрат зэрэгт дэвшүүлэх
    2. Дараах алдаануудыг зохих ёсоор барих:
       - ValueError: Хэрэглэгч тоо биш утга оруулсан үед
       - OverflowError: Үр дүн хэт их болсон үед
    """
    # Энд кодоо бичнэ үү
    try:
        number = int(input("Тоо оруулна уу: "))
        result = number **2
    except ValueError:
        print("Хэрэглэгч тоо биш утга оруулсан үед")
    except OverflowError:
        print("Үр дүн хэт их болсон үед")
    # else:
    #     print(result)

exercise_2()

# ===============================================================
# Дасгал 3: Else ба Finally блокууд
# ===============================================================


def exercise_3():
    
    """
    Else ба Finally блокуудыг ашиглах.

    Даалгавар:
    1. Хэрэглэгчээс файлын нэр аваад, тэр файлыг нээж агуулгыг харуулах
    2. Хэрэв файл олдохгүй бол зохих алдааны мессеж харуулах
    3. Файл амжилттай нээгдвэл Else блокт агуулгыг хэвлэх
    4. Finally блокт "Файл хаагдлаа" гэж хэвлэх
    """
    # Энд кодоо бичнэ үү
try:
# Эрсдэлтэй код2
    filename=(input("Neree oruulah:"))
    file = open(filename, "r" )
except FileNotFoundError:
    print("Файл олдоогүй!")
else:
    print("Файлын агуулга:\r")
finally:
    print("Файл хаагдлаа")

# ===============================================================
# Дасгал 4: Алдаа дамжуулах (re-raising)
# ===============================================================


def process_data(data):
    """
    Өгөгдлийг боловсруулж, алдаа гарвал дэлгэрэнгүй мэдээлэлтэйгээр дамжуулах.

    Даалгавар:
    1. data-г тоо руу хөрвүүлэх оролдлого хийх
    2. Хэрэв ValueError гарвал, алдааг барьж дэлгэрэнгүй мессежтэйгээр дахин өргөх
    """
    # Энд кодоо бичнэ үү
    try:
        abc=int(data)
        return abc
    except ValueError:
        raise ValueError(" Алдааг боловсруулж байна...")


def exercise_4():
    """
    Алдаа дамжуулах жишээг турших.

    Даалгавар:
    1. process_data функцийг дуудаж, алдаа барих
    2. "abc" утгыг дамжуулж, алдааг хэрхэн дамжуулж байгааг харах
    """
    # Энд кодоо бичнэ үү
    try:
       data= process_data(input("utag og:"))
    except ValueError:
        print("Aldaa")
        
    
exercise_4()

# ===============================================================
# Дасгал 5: Файл боловсруулах алдаа
# ===============================================================


def safe_open_file(filename):
    """
    Файлыг аюулгүй нээх функц.

    Даалгавар:
    1. Дараах алдаануудыг зохих ёсоор барих:
       - FileNotFoundError: Файл олдохгүй үед
       - PermissionError: Файлыг нээх эрх хүрэлцэхгүй үед
       - IsADirectoryError: filename нь файл биш, хавтас байх үед
    2. Алдаа гарвал None буцаах, амжилттай бол файлын объектыг буцаах
    """
    # Энд кодоо бичнэ үү
    try:
        file = open(filename)
        return file
    except FileNotFoundError:
        print(f"Алдаа: Файл {filename} олдсонгүй.")
    except PermissionError:
        print(f"Алдаа: Файлыг нээх эрх байхгүй: {filename}")
    except IsADirectoryError:
        print(f"Алдаа: {filename} нь файл биш бөгөөд хавтас.")
    except Exception as e:
        print(f"Тухайн алдаа гарлаа: {e}")
    return None 


def exercise_5():
    """
    safe_open_file функцийг турших.

    Даалгавар:
    1. Байхгүй файл, хавтас, эрх хүрэлцэхгүй файлуудаар туршилт хийх
    2. Амжилттай нээгдсэн файлын агуулгыг хэвлэх
    """
    # Энд кодоо бичнэ үү
   
exercise_5()
# ===============================================================
# Дасгал 6: Дахин оролдох загвар (Retry pattern)
# ===============================================================


def retry(func, max_attempts=3):
    """
    Функцийг хэд хэдэн удаа дахин оролдох декоратор.

    Даалгавар:
    1. Функцийг дуудаж, алдаа гарвал дахин оролдох
    2. max_attempts хүртэл оролдох
    3. Бүх оролдлого амжилтгүй бол сүүлийн алдааг дамжуулах
    """
    # Энд кодоо бичнэ үү
    pass


# Энэ функцийг retry декоратороор чимэглэнэ үү
def unstable_function():
    """Санамсаргүйгээр алдаа заримдаа гаргадаг функц."""
    import random

    if random.random() < 0.7:  # 70% магадлалтайгаар алдаа гаргана
        raise ConnectionError("Холболт тасарлаа")
    return "Амжилттай!"


def exercise_6():
    """
    Retry декораторыг турших.

    Даалгавар:
    1. unstable_function-г retry декоратороор чимэглэх
    2. Функцийг дуудаж, үр дүнг харах
    """
    # Энд кодоо бичнэ үү
    pass


def run_all_exercises():
    """
    Run all exercises in sequence.

    Даалгавар:
    1. Бүх дасгалуудыг дуудах
    2. Алдаа гарвал тухайн дасгалыг алгасаад дараагийнх руу шилжих
    """
    exercises = [
        exercise_1,
        exercise_2,
        exercise_3,
        exercise_4,
        exercise_5,
        exercise_6,
    ]

    for i, exercise in enumerate(exercises, 1):
        print(f"\n{'='*50}")
        print(f"Дасгал {i} ажиллаж байна:")
        print(f"{'='*50}")
        try:
            exercise()
        except Exception as e:
            print(f"Дасгал {i} алдаа гарлаа: {type(e).__name__}: {e}")
        print(f"{'='*50}")
        print(f"Дасгал {i} дууслаа.")
        print(f"{'='*50}\n")


if __name__ == "__main__":
    # Энд аль дасгалыг ажиллуулахаа сонгоно уу
    # Жишээ нь: exercise_1()
    # Эсвэл бүх дасгалыг ажиллуулах: run_all_exercises()
    pass