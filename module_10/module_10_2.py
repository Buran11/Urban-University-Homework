# 2023/12/10 00:00|Домашнее задание по теме "Потоки на классах"
from threading import Thread
from time import sleep


class Knight(Thread):
    '''
    Класс Рыцарь. Создаёт новый поток.
    '''

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemy = 100
        days = 0
        print(f'{self.name}, на нас напали!')
        while enemy > 0:
            enemy -= self.power
            days += 1
            print(f'{self.name} сражается {days}..., осталось {enemy} воинов.')
            sleep(1)
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


def main():
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight('Sir Galahad', 20)
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()


if __name__ == '__main__':
    main()
