# 2023/11/02 00:00|Домашняя работа по уроку "Различие атрибутов класса и экземпляра."
class House:
    houses_history = []

    def __new__(cls, *args):
        return super().__new__(cls)

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor
        House.houses_history.append(self.name)
    # Использовал регион для упрощения проверки
    # region Готовые задания из module_5_1, module_5_2, module_5_3

    def go_to(self, new_floor):
        if new_floor > self.number_of_floor or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(f'Этаж {i + 1}')

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floor}'

    def __verify_data(self, other):
        # Проверка атрибутов на тип данных
        if not isinstance(other, (House, int)) and not isinstance(self, (House, int)):
            raise TypeError(
                'Атрибут "other" должен пренадлежать типу "House" или "int"')

    def __eq__(self, other):
        self.__verify_data(other)
        if isinstance(other, int):
            return self.number_of_floor == other
        elif isinstance(other, House):
            return self.number_of_floor == other.number_of_floor

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

    def __add__(self, value):
        self.__verify_data(value)
        if isinstance(value, int):
            self.number_of_floor += value
        elif isinstance(value, House):
            self.number_of_floor += value.number_of_floor
        return self

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)
    # endregion

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


# Пример выполнения программы:
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

# Вывод на консоль:
# ['ЖК Эльбрус']
# ['ЖК Эльбрус', 'ЖК Акация']
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Акация снесён, но он останется в истории
# ЖК Матрёшки снесён, но он останется в истории
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Эльбрус снесён, но он останется в истории
