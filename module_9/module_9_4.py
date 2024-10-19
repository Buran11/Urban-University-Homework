# 2023/12/02 00:00|Домашнее задание по теме "Создание функций на лету"

from random import choice

# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'


# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for string in data_set:
                file.write(f'{string}\n')
    return write_everything


# Метод __call__:
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


def main():
    # Lambda-функция:
    print(list(map(lambda x, y: x == y, first, second)))

    # Замыкание:
    write = get_advanced_writer('example.txt')
    write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

    # Метод __call__:
    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print(first_ball())
    print(first_ball())
    print(first_ball())


if __name__ == '__main__':
    main()
