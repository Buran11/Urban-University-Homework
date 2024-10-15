# 2023/11/25 00:00|Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции".

def personal_sum(numbers):
    '''
    Функция подсчета суммы числовых значений из списка
    и значений с некорректным типом данных.
    Возвращает кортеж: (result, incorrect_data)
        result - сумма числовых значений
        incorrect_data - количество некорректных типов данных
    Так же обрабатывает исключения TypeError    
    '''
    incorrect_data = 0
    result = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    '''
    Функция подсчета среднего арифметического
    Все значения должны быть числовыми-положительными, иначе
    функция обработает исключения TypeError и ZeroDivisionError
    '''
    arithmeti_mean = 0
    int_elements = []
    try:
        for i in numbers:
            if not isinstance(i, (str, float)):
                int_elements.append(i)
        arithmeti_mean = personal_sum(numbers)[0] / len(int_elements)
        return arithmeti_mean
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        return None
    except ZeroDivisionError:
        return 0


def main():
    # Проверка функции personal_sum
    # print(f'Результат 1: {personal_sum("1, 2, 3")}')
    # print(f'Результат 2: {personal_sum([1, "Строка", 3, "Ещё Строка"])}')
    # print(f'Результат 3: {personal_sum(567)}')
    # print(f'Результат 4: {personal_sum([42, 15, 36, 13])}')

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
