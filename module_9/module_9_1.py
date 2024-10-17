# 2023/11/29 00:00|Домашнее задание по теме "Введение в функциональное программирование"

def apply_all_func(int_list, *functions):
    '''
    Задача "Вызов разом"
    '''
    result = {}
    try:
        for func in functions:
            result[func.__name__] = func(int_list)
    except TypeError as exc:
        print('Некорректный тип данных', exc)
    return result


def main():
    print(apply_all_func([6, 'ee', 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))


# Точка входа
if __name__ == '__main__':
    main()
