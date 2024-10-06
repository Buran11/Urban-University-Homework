# 2023/11/08 00:00|Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."

class Vehicle:
    '''
    Базовый класс "Транспортное средство".
    Атрибуты класса:
    __COLOR_VARIANT - список возможных цветов.
    Атрибуты объекта:
    owner - владелец, __model - модель, __engine_power - мощность двигателя,
    __color - цвет.
    Методы: get_model - возвращает модель, get_horsepower - возвращает мощность двигателя,
    get_color - возвращает цвет, print_info - выводит информацию о транспортном средстве,
    set_color - меняет цвет.
    '''
    __COLOR_VARIANT = ['blue', 'red', 'green', 'black', 'white']
    # __COLOR_VARIANT = []

    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    # Записываем список вариантов цветов
    # def set_colors_variant(self, colors_variant_list: list):
    #     self.__COLOR_VARIANT = colors_variant_list

    def get_model(self):
        return 'Модель: ' + self.__model

    def get_horsepower(self):
        return 'Мощность двигателя: ' + str(self.__engine_power)

    def get_color(self):
        return 'Цвет: ' + str(self.__color)

    def print_info(self):
        print(self.get_model() + '\n' + self.get_horsepower() + '\n' +
              self.get_color() + '\n' + 'Владелец: ' + str(self.owner))

    def set_color(self, new_color: str):
        for color in self.__COLOR_VARIANT:
            if color.casefold() == new_color.casefold():
                self.__color = new_color
                break
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    '''
    Класс "Седан".
    Наследник класса Vehicle - "Транспортное средство".
    Атрибуты класса:
    __PASSENGERS_LIMIT - лимит пассажиров. 
    '''
    __PASSENGERS_LIMIT = 5

# Вывод на консоль:
# Модель: Toyota Mark II
# Мощность двигателя: 500
# Цвет: blue
# Владелец: Fedos
# Нельзя сменить цвет на Pink
# Модель: Toyota Mark II
# Мощность двигателя: 500
# Цвет: BLACK
# Владелец: Vasyok


# Точка входа
if __name__ == '__main__':
    # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
    ###
    # Записываем список вариантов цветов
    # colors_variant_list = ['blue', 'red', 'green', 'black', 'white', 'pink']
    # vehicle1.set_colors_variant(colors_variant_list)
    ###
    # Изначальные свойства
    vehicle1.print_info()
    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'
    # Проверяем что поменялось
    vehicle1.print_info()
