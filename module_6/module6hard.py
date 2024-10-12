# 2023/11/12 00:00|Дополнительное практическое задание по модулю*

import logging
from math import pi
from math import sqrt


class Figure():
    ''' Базовый класс - Фигура '''
    sides_count = 0

    def __init__(self, __color: list, __sides: list, filled: bool = False):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled

    def get_color(self):
        # logging.info("Цвет фигуры: %s", self.__color)
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int):
        if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
            # logging.warning("Цвет должен быть в диапазоне от 0 до 255")
            return False
        if not isinstance(r, int) and not isinstance(g, int) and not isinstance(b, int):
            # logging.warning("Цвет должен быть целым числом")
            return False
        return True

    def set_color(self, r: int, g: int, b: int):
        if not self.__is_valid_color(r, g, b):
            # logging.warning("Некорректный цвет")
            return
        # logging.info("Новый цвет: %s", [r, g, b])
        self.__color = [r, g, b]

    def __is_valided_sides(self, *sides):
        if len(sides) != self.sides_count:
            # logging.warning("Неверное количество сторон")
            return False
        if not all(isinstance(i, int) for i in sides):
            # logging.warning("Стороны должны быть целыми числами")
            return False
        return True

    def get_sides(self):
        # logging.info("Стороны: %s", self.__sides)
        return self.__sides

    def __len__(self):
        perimeter = 0
        for i in self.__sides:
            perimeter += i
        return perimeter

    def set_sides(self, *new_sides):
        ls_sides = []
        if not self.__is_valided_sides(new_sides):
            # logging.warning("Некорректные стороны")
            for i in range(self.sides_count):
                ls_sides.append(self.__sides)
            self.__sides = ls_sides
        else:
            # logging.info("Новые стороны: %s", new_sides)
            for i in range(self.sides_count):
                ls_sides.append(1)
            self.__sides = new_sides
        if len(new_sides) == self.sides_count:
            # logging.info("Новая сторона: %s", new_sides)
            self.__sides = list(new_sides)


class Circle(Figure):
    ''' Круг '''
    sides_count = 1

    def get_radius(self):
        self.__radius = super().get_sides()[0] / (pi*2)
        # logging.info("Радиус круга: %s", self.__radius)
        return round(self.__radius, 2)

    def get_square(self):
        s_radius = pi * self.__radius**2
        # logging.info("Площадь круга от радиуса: %s", s_radius)
        s_length = super().get_sides()[0]**2/(pi*4)
        # logging.info("Площадь круга от длинны: %s", s_length)
        return f'S от radius = {round(s_radius, 2)}' + '\n' + f'S от Lenght = {round(s_length, 2)}'


class Triangle(Figure):
    ''' Треугольник '''
    sides_count = 3

    def get_square(self):
        p = super().__len__() / 2
        s_triangle = sqrt(
            p * (p - super().get_sides()[0]) * (p - super().get_sides()[1]) * (p - super().get_sides()[2]))
        # logging.info("Площадь треугольника: %s", s_triangle)
        return round(s_triangle, 2)
        pass


class Cube(Figure):
    ''' Куб '''
    sides_count = 12

    def get_volume(self):
        return super().get_sides()[0] ** 3


# Выходные данные (консоль):
# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216


# Точка входа
if __name__ == '__main__':
    # Логирование в консоль
    # logging.basicConfig(level=logging.INFO,
    #                     format="%(asctime)s %(levelname)s %(message)s")

    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

    # # Проверка радиуса (круга):
    # print(circle1.get_radius())

    # # Проверка площади (круга):
    # print(circle1.get_square())

    # # Проверка (треугольника):
    # triangle = Triangle((15, 15, 15), 3)
    # print(triangle.get_sides())
    # triangle.set_sides(4, 4, 4)
    # print(triangle.get_sides())
    # print(len(triangle))
    # print(triangle.get_square())
