# 2023/10/31 00:00|Домашняя работа по уроку "Перегрузка операторов."

class House:
    # Инструкция к module_5_1
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if new_floor > self.number_of_floor or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(f'Этаж {i + 1}')

    # Инструкция к module_5_2
    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floor}'

    # Инструкция к module_5_3
    def __verify_data(self, other):
        # Проверка атрибутов на тип данных
        if not isinstance(other, (House, int)) and not isinstance(self, (House, int)):
            raise TypeError(
                'Атрибут "other" должен пренадлежать типу "House" или "int"')
    # 1

    def __eq__(self, other):
        self.__verify_data(other)
        if isinstance(other, int):
            return self.number_of_floor == other
        elif isinstance(other, House):
            return self.number_of_floor == other.number_of_floor

    # 2

    def __lt__(self, other):
        self.__verify_data(other)
        if isinstance(other, int):
            return self.number_of_floor < other
        elif isinstance(other, House):
            return self.number_of_floor < other.number_of_floor
        return self.number_of_floor < other.number_of_floor

    def __le__(self, other):
        self.__verify_data(other)
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        self.__verify_data(other)
        return not self.__le__(other)

    def __ge__(self, other):
        self.__verify_data(other)
        return not self.__lt__(other)

    def __ne__(self, other):
        self.__verify_data(other)
        return not self.__eq__(other)

    # 3
    def __add__(self, value):
        self.__verify_data(value)
        if isinstance(value, int):
            self.number_of_floor += value
        elif isinstance(value, House):
            self.number_of_floor += value.number_of_floor
        return self

    # 4
    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__


# Вывод на консоль:
# Название: ЖК Эльбрус, кол-во этажей: 10
# Название: ЖК Акация, кол-во этажей: 20
# False
# Название: ЖК Эльбрус, кол-во этажей: 20
# True
# Название: ЖК Эльбрус, кол-во этажей: 30
# Название: ЖК Акация, кол-во этажей: 30
# False
# True
# False
# True
# False
