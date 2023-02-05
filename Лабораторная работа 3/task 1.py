class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name  # инициализируем защищенный атрибут
        self._author = author  # инициализируем защищенный атрибут

    @property
    def name(self) -> str:
        return self._name  # внутри класса обращаемся к защищенному атрибуту self._name

    @property
    def author(self) -> str:
        return self._author  # внутри класса обращаемся к защищенному атрибуту self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс - бумажные книги. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)  # вызываем конструктор родительского класса
        self.pages = pages

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def pages(self) -> str:
        return self.pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным")


class AudioBook(Book):
    """ Дочерний класс - электронные книги. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)  # вызываем конструктор родительского класса
        self.duration = duration

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def duration(self) -> str:
        return self.duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError("Длительность должна быть типа float")
        if duration < 0:
            raise ValueError("Длительность не может быть отрицательной")
# конец кода
