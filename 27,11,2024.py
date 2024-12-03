class Course:
    """
    Класс, представляющий курс.
    """
    def __init__(self, title: str, duration: int) -> None:
        """
        Создание и подготовка к работе объекта класса Course (Курс)

        :param title: str: Название курса
        :param duration: int: Продолжительность курса в неделях
        """
        self.title: str = title
        self.duration: int = duration

    def get_absolute_url(self) -> str:
        """
        Возвращает абсолютный URL курса.

        :return: str
        """
        return f"https://ivashev-edu.com/courses/{self.title}"

class StudentProfile:
    """
    Класс, представляющий профиль студента.
    """
    def __init__(self, full_name: str, email: str) -> None:
        """
        Создание и подготовка к работе объекта класса StudentProfile (Профиль студента)

        :param full_name: str: Полное имя студента
        :param email: str: Электронная почта студента
        """
        self.full_name: str = full_name
        self.email: str = email

    def get_absolute_url(self) -> str:
        """
        Возвращает абсолютный URL профиля студента.

        :return: str
        """
        return f"https://ivashev-edu.com/profiles/{self.full_name.lower().replace(' ', '')}"

# Create course objects
course1: Course = Course("Python-Basics", 12)
course2: Course = Course("Web Development", 16)

# Create student profile objects
student1: StudentProfile = StudentProfile("John Doe", "john.doe@example.com")
student2: StudentProfile = StudentProfile("Jane Smith", "jane.smith@example.com")

# Print absolute URLs
print(course1.get_absolute_url())
print(course2.get_absolute_url())
print(student1.get_absolute_url())
print(student2.get_absolute_url())
