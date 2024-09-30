# 2023/10/30 00:00|Домашняя работа по уроку "Специальные методы классов"

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


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

# Вывод на консоль:
# Название: ЖК Эльбрус, кол-во этажей: 10
# Название: ЖК Акация, кол-во этажей: 20
# 10
# 20
