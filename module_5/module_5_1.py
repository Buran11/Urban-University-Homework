# 2023/10/29 00:00|Домашняя работа по уроку "Атрибуты и методы объекта."

class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if new_floor > self.number_of_floor or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(f'Этаж {i + 1}')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

# Вывод на консоль:
# Этаж 1
# Этаж 2
# Этаж 3
# Этаж 4
# Этаж 5
# Такого этажа не существует
