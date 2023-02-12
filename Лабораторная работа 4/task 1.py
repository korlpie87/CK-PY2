from typing import Union


class MovieDiary:
    def __init__(self, name: str, director: str, rating: Union[int, float]):
        """
        Базовый класс - Кинодневник.

        :param name: Название кинопроизведения
        :param director: Режиссёр
        :param rating: Личный рейтинг

        Пример:
        >>> movie_1 = MovieDiary ("Чебурашка", "Дмитрий Дьяченко", 8)
        """
        self.name = name
        self.director = director
        self.rating = rating

    # свойства с проверками при присвоении значений атрибуту rating:
    @property
    def rating(self) -> str:
        return self.rating

    @rating.setter
    def rating(self, rating: Union[int, float]) -> None:
        if not isinstance(rating, (int, float)):
            raise TypeError("Рейтинг должен быть типа int или float")
        if rating < 0:
            raise ValueError("Рейтинг не может быть отрицательным")

    def sum_movie(self) -> int:
        """
        Функция показывает общее количество просмотренных фильмов и сериалов, занесённых в кинодневник.
        """
        ...

    def favorite_director(self) -> str:
        """
        Функция показывает наиболее часто встречающегося режиссёра в кинодневнике.
        """
        ...

    def sum_hours(self) -> (int, float):
        """
        Функция показывает общее количество часов, уделённых просмотру фильмов и сериалов.
        """
        ...

    def random_film(self) -> str:
        """
        Функция выдаёт случайный фильм или сериал из кинодневника.
        """
        ...

    def __str__(self) -> str:
        return f"Кинопроизведение {self.name}. Режиссёр {self.director}. Оценка {self.rating}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, director={self.director!r}, rating{self.rating!r})"


class Movies(MovieDiary):
    def __init__(self, name: str, director: str, rating: Union[int, float], duration: Union[int, float]):
        """
        Дочерний класс - Фильмы.

        :param name: Название
        :param director: Режиссёр
        :param rating: Личный рейтинг
        :param duration: Длительность фильма в минутах

        Пример:
        >>> movie_1 = MovieDiary ("Чебурашка", "Дмитрий Дьяченко", 8, 113)
        """
        super().__init__(name, director, rating)  # вызываем конструктор родительского класса
        self.duration = duration

    # свойства с проверками при присвоении значений атрибуту duration:
    @property
    def duration(self) -> str:
        return self.duration

    @duration.setter
    def duration(self, duration: Union[int, float]) -> None:
        if not isinstance(duration, (int, float)):
            raise TypeError("Длительность фильма должна быть типа int или float")
        if duration <= 0:
            raise ValueError("Длительность фильма не может быть отрицательной или равной нулю")

    def sum_hours(self) -> (int, float):
        """
        Функция показывает общую длительность (в часах) всех фильмов, занесённых в кинодневник.
        Метод перегружен в дочерний класс, так как функция учитывает только длительность фильмов.
        """
        ...

    def random_film(self) -> str:
        """
        Функция возвращает случайный фильм из кинодневника.
        Метод перегружен в дочерний класс, так как функция учитывает только фильмы.
        """
        ...

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, director={self.director!r}, rating{self.rating!r})"


class Series(MovieDiary):
    def __init__(self, name: str, director: str, rating: Union[int, float], minutes: int, series: int, season: int):
        """
        Дочерний класс - Сериалы.

        :param name: Название
        :param director: Режиссёр
        :param rating: Личный рейтинг
        :param minutes: Длительность одной серии в минутах
        :param series: Среднее количество серий в одном сезоне
        :param season: Количество сезонов

        Пример:
        >>> movie_2 = MovieDiary ("Отчаянные домохозяйки", "Дэвид Гроссман", 8, 43, 23, 8)
        """
        super().__init__(name, director, rating)  # вызываем конструктор родительского класса
        self.series = series
        self.season = season
        self.minutes = minutes

    # свойства с проверками при присвоении значений атрибуту minutes:
    @property
    def minutes(self) -> str:
        return self.minutes

    @minutes.setter
    def minutes(self, minutes: int) -> None:
        if not isinstance(minutes, int):
            raise TypeError("Длительность одной серии должна быть типа int")
        if minutes <= 0:
            raise ValueError("Длительность одной серии не может быть отрицательной или равной нулю")

    # свойства с проверками при присвоении значений атрибуту series:
    @property
    def series(self) -> str:
        return self.series

    @series.setter
    def series(self, series: int) -> None:
        if not isinstance(series, int):
            raise TypeError("Среднее количество серий в одном сезоне должно быть типа int")
        if series <= 0:
            raise ValueError("Среднее количество серий в одном сезоне не может быть отрицательным или равным нулю")

    # свойства с проверками при присвоении значений атрибуту season:
    @property
    def season(self) -> str:
        return self.season

    @season.setter
    def season(self, season: int) -> None:
        if not isinstance(season, int):
            raise TypeError("Количество сезонов должно быть типа int")
        if season <= 0:
            raise ValueError("Количество сезонов не может быть отрицательным или равным нулю")

    def sum_hours(self) -> (int, float):
        """
        Функция показывает общую длительность всех сериалов, занесённых в кинодневник.
        Метод перегружен в дочерний класс, так как функция учитывает только длительность сериалов.
        """
        ...

    def random_film(self) -> str:
        """
        Функция возвращает случайный сериал из кинодневника.
        Метод перегружен в дочерний класс, так как функция учитывает только сериалы.
        """
        ...

    def max_season(self) -> int:
        """
        Функция возвращает название сериала с наибольшим количеством сезонов.
        """
        ...

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, director={self.director!r}, rating{self.rating!r})"


if __name__ == "__main__":
    pass
