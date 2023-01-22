import doctest
from typing import Union


# Первый класс
class Hamster:
    def __init__(self, maximum_energy: int, current_energy: int):
        """
        Создание и подготовка к работе объекта "Хомяк"

        :param maximum_energy: Максимальное количество энергии хомяка
        :param current_energy: Текуще количество энергии хомяка

        Пример:
        >>> hamster = Hamster (100, 99)  # инициализация экземпляра класса
        """
        if not isinstance(maximum_energy, int):
            raise TypeError("Количество макс. энергии должно быть типа int")
        if maximum_energy <= 0:
            raise ValueError("Количество макс. энергии не должно быть меньше нуля или равно нулю")
        self.maximum_energy = maximum_energy

        if not isinstance(current_energy, int):
            raise TypeError("Количество текущей энергии должно быть типа int")
        if current_energy < 0:
            raise ValueError("Количество текущей энергии не должно быть меньше нуля")
        self.current_energy = current_energy

    def amount_energy(self) -> bool:
        """
        Функция проверяет достаточно ли энергии у хомяка, сранивая текущее значение энергии с неким числом

        :return: Достаточно ли энергии у хомяка

        Пример:
        >>> hamster = Hamster(100, 100)
        >>> hamster.amount_energy()
        """
        ...

    def run_wheel(self, required_energy: int) -> None:
        """
        Функция позволяет хомяку побегать в колесе, если затрачиваемая на это энергия меньше имеющейся (текущей)

        :param required_energy: Количество требуемой энергии

        :raise ValueError: Если текущее количество энергии недостаточно, то вызываем ошибку

        :return: Хомяк бегает в колесе

        Пример:
        >>> hamster = Hamster(100,90)
        >>> hamster.run_wheel(20)
        """
        if not isinstance(required_energy, int):
            raise TypeError("Требуемая энергия должна быть типа int")
        if required_energy < 0:
            raise ValueError("Требуемая энергия должна быть положительна")
        ...

    def go_eat_and_sleep(self) -> bool:
        """
        Функция, которая отправляет хомяка отдыхать

        :return: Хомяк ушёл отдыхать

        Пример:
        >>> hamster = Hamster(100, 50)
        >>> hamster.go_eat_and_sleep()
        """
        ...


# Второй класс
class Bus:
    def __init__(self, fuel_quantity: Union[int, float], fuel_consumption: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Автобус"
        :param fuel_quantity: Количество топлива, л
        :param fuel_consumption: Расход топлива на пробег автобуса, л/100 км

        Пример:
        >>> bus = Bus(50, 30) # инициализация экземпляра класса
        """
        if not isinstance(fuel_quantity, (int, float)):
            raise TypeError("Количество топлива должно быть типа int или float")
        if fuel_quantity < 0:
            raise ValueError("Количество топлива не может быть меньше нуля")
        self.fuel_quantity = fuel_quantity

        if not isinstance(fuel_consumption, (int, float)):
            raise TypeError("Расход топлива должен быть типа int или float")
        if fuel_consumption <= 0:
            raise ValueError("Расход топлива не может быть отрицательным или равным нулю")
        self.fuel_consumption = fuel_consumption

    def start_engine(self) -> bool:
        """
        Функция, которая запускает двигатель, если есть топливо

        :return: "Двигатель запущен"

        Пример:
        >>> bus = Bus(70, 40)
        >>> bus.start_engine()
        """
        ...

    def what_distance(self, distance: Union[int, float]) -> None:
        """
        Функция, которая показывает, можно ли проехать нужное расстояние при текущем уровне топлива

        :param distance: Дальность поездки, км

        :raise ValueError: Если топлива не хватит, то вызываем ошибку

        Пример:
        >>> bus = Bus(50, 30)
        >>> bus.what_distance(20)
        """
        if not isinstance(distance, (int, float)):
            raise TypeError("Расстояние должно быть типа int или float")
        if distance <= 0:
            raise ValueError("Расстояние не может быть отрицательным или равным нулю")
        ...


# Третий класс
class MoneyBox:
    def __init__(self, money: int, time: int):
        """
        Создание и подготовка к работе объекта "Копилка"

        :param money: цель, т.е. сумма, которую нужно накопить, руб.
        :param time: срок, за который необходимо накопить, мес.

        Пример:
        >>> box1 = MoneyBox(10000, 2)  # инициализация экземпляра класса
        """
        if not isinstance(money, int):
            raise TypeError("Сумма должна быть типа int")
        if money < 0:
            raise ValueError("Сумма должна быть положительной")
        self.money = money

        if not isinstance(time, int):
            raise TypeError("Срок должен быть типа int")
        if time < 0:
            raise ValueError("Срок должен быть положительным")
        self.time = time

    def add_money(self, new_money: int) -> None:
        """
        Добавление некоторой суммы в копилку

        :param new_money: Размер внесённой суммы, руб

        Пример:
        >>> money_box = MoneyBox(10000, 2)
        >>> money_box.add_money(1000)
        """
        if not isinstance(new_money, (int, float)):
            raise TypeError("Размер внесённой суммы должен быть типа int или float")
        if new_money < 0:
            raise ValueError("Размер внесённой суммы должен быть положительным")
        ...

    def money_rest(self) -> None:
        """
        Рассчитывает оставшуюся сумму, которую нужно внести для достижения цели в срок

        :return: Недостающая сумма

        Пример:
        >>> money_box = MoneyBox(10000, 2)
        >>> money_box.money_rest()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # проверка работоспособности классса с помощью doctest
    pass

# конец кода
