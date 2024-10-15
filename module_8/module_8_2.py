# 2023/11/25 00:00|Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции".

def personal_sum(*numbers):
    incorrect_data = 0
    result = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(*numbers):
    arithmetic_mean = 0
    try:
        for i in numbers:
            for j in i:
                try:
                    arithmetic_mean = personal_sum(j, arithmetic_mean)[
                        0] / len(numbers)
                    return arithmetic_mean
                except TypeError:
                    f'В numbers записан некорректный тип данных - {j}'
                    return None
    except ZeroDivisionError:
        return 0


# Вывод на консоль:
# Некорректный тип данных для подсчёта суммы - 1
# Некорректный тип данных для подсчёта суммы - ,
# Некорректный тип данных для подсчёта суммы -
# Некорректный тип данных для подсчёта суммы - 2
# Некорректный тип данных для подсчёта суммы - ,
# Некорректный тип данных для подсчёта суммы -
# Некорректный тип данных для подсчёта суммы - 3
# Результат 1: 0
# Некорректный тип данных для подсчёта суммы - Строка
# Некорректный тип данных для подсчёта суммы - Ещё Строка
# Результат 2: 2.0
# В numbers записан некорректный тип данных
# Результат 3: None
# Результат 4: 26.5


def main():
    # проверка функции personal_sum
    # print(f'Результат 1: {personal_sum(1, 2, 3, 'qqqq')}')

    # Пример выполнения программы:
    # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 1: {calculate_average("1, 2, 3")}')
    # Учитываются только 1 и 3
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
    print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
    # Всё должно работать
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')

    # Точка входа
if __name__ == '__main__':
    main()
