"""
Дасгал 1: Үндсэн Удамшил.

------------------------
Доорх Тээврийн хэрэгсэл (Vehicle) классын бүтцийг гүйцээнэ үү.
- Vehicle-ээс удамшсан Car болон Motorcycle классуудыг хэрэгжүүлнэ үү
- Тохирох аттрибут болон методуудыг нэмнэ үү
- Дэд классуудад display_info методыг дахин тодорхойлно уу
"""


class Vehicle:
    """Тээврийн хэрэгслийн үндсэн класс."""

    def __init__(self, make: str, model: str, year: int):
        """Vehicle классын байгуулагч.

        Args:
            make: Үйлдвэрлэгч
            model: Загвар
            year: Үйлдвэрлэсэн он
        """
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self) -> str:
        """Тээврийн хэрэгслийг асаах."""
        self.is_running = True
        return f"{self.make} {self.model} асаалаа"

    def stop(self) -> str:
        """Тээврийн хэрэгслийг унтраах."""
        self.is_running = False
        return f"{self.make} {self.model} унтраалаа"

    def display_info(self) -> str:
        """Тээврийн хэрэгслийн мэдээллийг харуулах."""
        return f"{self.year} оны {self.make} {self.model}"


# TODO: Vehicle-ээс удамшсан Car классыг хэрэгжүүлнэ үү
# Car нь нэмэлт аттрибуттай байх: num_doors, fuel_type
# display_info-г дахин тодорхойлж эдгээр аттрибутуудыг оруулна уу


# TODO: Vehicle-ээс удамшсан Motorcycle классыг хэрэгжүүлнэ үү
# Motorcycle нь нэмэлт аттрибуттай байх: engine_cc, has_sidecar
# display_info-г дахин тодорхойлж эдгээр аттрибутуудыг оруулна уу


"""
Дасгал 2: Метод дахин тодорхойлох ба super().

--------------------------------------------
Доорх Дүрс (Shape) классын бүтцийг гүйцээнэ үү.
- Rectangle болон Circle классуудыг хэрэгжүүлнэ үү
- super()-г ашиглан эцэг классын функционалыг өргөтгөнө үү
- Тус бүр дүрсийн талбай болон периметрийг тооцоолно уу
"""


class Shape:
    """Дүрсийн үндсэн класс."""

    def __init__(self, color: str):
        """Shape классын байгуулагч.

        Args:
            color: Дүрсийн өнгө
        """
        self.color = color

    def area(self) -> float:
        """Дүрсийн талбайг тооцоолох."""
        pass  # Дахин тодорхойлогдох абстракт метод

    def perimeter(self) -> float:
        """Дүрсийн периметрийг тооцоолох."""
        pass  # Дахин тодорхойлогдох абстракт метод

    def describe(self) -> str:
        """Дүрсийн талаар мэдээлэл өгөх."""
        return f"{self.color} өнгөтэй дүрс"


# TODO: Rectangle классыг хэрэгжүүлнэ үү
# Rectangle нь өргөн ба өндөр аттрибуттай байх
# area, perimeter, болон describe методуудыг дахин тодорхойлно уу


# TODO: Circle классыг хэрэгжүүлнэ үү
# Circle нь радиус аттрибуттай байх
# area, perimeter, болон describe методуудыг дахин тодорхойлно уу
# Тооцоололд math.pi-г ашиглана уу


"""
Дасгал 3: Олон Удамшил.

---------------------
Доорх Ажилтан (Employee) бүтцийг миксинуудтай хамт гүйцээнэ үү.
- Manager болон Developer классуудыг хэрэгжүүлнэ үү
- Өгөгдсөн миксинуудыг ашиглан функционал нэмнэ үү
- Жишээнүүд үүсгэж бүх методуудын хэрэглээг харуулна уу
"""


class EmailMixin:
    """Имэйл илгээх функционал нэмэх миксин."""

    def send_email(self, message: str) -> str:
        """Имэйл илгээх.

        Args:
            message: Илгээх зурвас

        Returns:
            Имэйл илгээсэн тухай мэдээлэл
        """
        return f"{self.email} хаяг руу имэйл илгээж байна: {message}"


class ReportMixin:
    """Тайлан үүсгэх функционал нэмэх миксин."""

    def generate_report(self) -> str:
        """Тайлан үүсгэх.

        Returns:
            Тайлан үүсгэсэн тухай мэдээлэл
        """
        return f"{self.name}-н тайланг үүсгэж байна"


class Employee:
    """Ажилтны үндсэн класс."""

    def __init__(self, name: str, employee_id: str, email: str):
        """Employee классын байгуулагч.

        Args:
            name: Ажилтны нэр
            employee_id: Ажилтны дугаар
            email: Ажилтны имэйл хаяг
        """
        self.name = name
        self.employee_id = employee_id
        self.email = email

    def display_info(self) -> str:
        """Ажилтны мэдээллийг харуулах."""
        return f"Ажилтан: {self.name}, ID: {self.employee_id}"


# TODO: Employee болон хоёр миксинээс удамшсан Manager классыг хэрэгжүүлнэ үү
# department болон team_size аттрибутуудыг нэмнэ үү


# TODO: Employee болон EmailMixin-ээс удамшсан Developer классыг хэрэгжүүлнэ үү
# programming_languages болон projects аттрибутуудыг нэмнэ үү


"""
Дасгал 4: Капсулжуулалт.

---------------------
Доорх Бүтээгдэхүүн (Product) классын зөв капсулжуулалтыг хэрэгжүүлнэ үү.
- Хувийн болон хамгаалагдсан аттрибутуудыг зохистой ашиглана уу
- Property декораторуудыг хэрэгжүүлж хяналттай хандалт хийнэ үү
- Setter-үүдэд баталгаажуулалт нэмнэ үү
"""


class Product:
    """Бүтээгдэхүүний класс."""

    def __init__(self, name: str, price: float, stock: int):
        """Product классын байгуулагч.

        Args:
            name: Бүтээгдэхүүний нэр
            price: Бүтээгдэхүүний үнэ
            stock: Бүтээгдэхүүний нөөц
        """
        # TODO: Аттрибутуудыг тохирох харагдацтай эхлүүлнэ үү
        pass

    # TODO: Бүх аттрибутуудад тохирох getter болон setter-тэй property-үүдийг хэрэгжүүлнэ үү
    # price нь сөрөг байж болохгүй
    # stock нь сөрөг бус бүхэл тоо байх ёстой

    # TODO: total_value (price * stock) тооцоолох метод хэрэгжүүлнэ үү


"""
Дасгал 5: Полиморфизм.

-------------------
Доорх полиморфик функц болон классуудыг хэрэгжүүлнэ үү.
- MediaItem удамшлын бүтцийг гүйцээнэ үү
- Аливаа MediaItem-тэй ажиллах play_media функцийг хэрэгжүүлнэ үү
- Тус бүр төрлийн жишээнүүд үүсгэж полиморфизмыг харуулна уу
"""


class MediaItem:
    """Медиа контентын үндсэн класс."""

    def __init__(self, title: str, duration: int):
        """Инициализирует экземпляр MediaItem.

        Args:
            title: Медиа контентын гарчиг
            duration: Медиа контентын үргэлжлэх хугацаа (секундээр)
        """
        self.title = title
        self.duration = duration

    def play(self) -> str:
        """Медиа контентыг тоглуулах."""
        pass  # Дахин тодорхойлогдох абстракт метод


# TODO: MediaItem-ээс удамшсан Song классыг хэрэгжүүлнэ үү
# artist болон genre аттрибутуудыг нэмнэ үү
# play методыг дахин тодорхойлно уу


# TODO: MediaItem-ээс удамшсан Movie классыг хэрэгжүүлнэ үү
# director болон rating аттрибутуудыг нэмнэ үү
# play методыг дахин тодорхойлно уу


# TODO: MediaItem-ээс удамшсан Podcast классыг хэрэгжүүлнэ үү
# host болон episode аттрибутуудыг нэмнэ үү
# play методыг дахин тодорхойлно уу


# TODO: Аливаа MediaItem авч тоглуулах play_media функцийг хэрэгжүүлнэ үү
# Энэ нь MediaItem-ийн аливаа дэд класстай полиморфик ажиллах ёстой


# Хэрэгжүүлэлтээ энд шалгана уу
if __name__ == "__main__":
    # Тохирох жишээнүүд болон метод дуудалтуудаар кодоо шалгана уу
    pass