# 2023/11/26 00:00|Домашнее задание по теме "Создание исключений"

class IncorrectVinNumber(Exception):
    '''
    Исключение IncorrectVinNumber - исключение, возникающее при некорректном
    формате данных для VIN номера.
    '''

    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    '''
    Исключение IncorrectCarNumbers - исключение, возникающее при некорректном
    формате данных для номеров машин.
    '''

    def __init__(self, message):
        self.message = message


class Car():
    '''
    Класс Car - модель машины.
    '''

    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers

        self.__is_valid_vin(self.__vin)
        self.__is_valid_car_numbers(self.__numbers)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_car_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers(
                'Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers(
                'Неверная длина номера')
        return True


def main():
    # Пример выполняемого кода:
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')


# Точка входа
if __name__ == '__main__':
    main()
