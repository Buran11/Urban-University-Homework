# 2023/11/24 00:00|Домашнее задание по теме "Try и Except".

def add_everything_up(a, b):
    '''
    Метод складывает числа(Int, Float) и строки(str)
    '''
    try:
        return round(a + b, 3)
    except TypeError:
        return f'{a}{b}'


def main():
    # Пример кода:
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))


# Точка входа
if __name__ == '__main__':
    main()
