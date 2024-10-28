# 2023/12/14 00:00|Домашнее задание по теме "Очереди для обмена данными между потоками."

from threading import Thread, current_thread
from time import sleep
from queue import Queue
from random import randint


class Table:
    '''
    Класс "Столик".
    Хранит информацию о находящемся за ним гостем (Guest).
    '''

    def __init__(self, number: int):
        self.number = number
        self.guest = None


class Guest(Thread):
    '''
    Класс "Гость".
    Поток, при запуске которого происходит задержка от 3 до 10 секунд.
    '''

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        delay = randint(3, 10)
        sleep(delay)


class Cafe:
    '''
    Класс "Кафе".
    В котором есть определённое кол-во столов и происходит имитация 
    прибытия гостей (guest_arrival) и их обслуживания (discuss_guests).
    '''
    threads_ls = []

    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests: Guest):
        difference_guests_tables = min(len(guests), len(self.tables))
        for i in range(difference_guests_tables):
            self.tables[i].guest = guests[i]
            thread_temp = guests[i]
            thread_temp.start()
            Cafe.threads_ls.append(thread_temp)
            print(
                f'{guests[i].name} сел(-а) за стол номер {self.tables[i].number}')
        if len(guests) > difference_guests_tables:
            for i in range(difference_guests_tables, len(guests)):
                self.queue.put(guests[i])
                print(f'{guests[i].name} в очереди')

    def discuss_guests(self):
        while not (self.queue.empty()) or table.guest is not None:
            for table in self.tables:
                if not (table.guest is None) and not (table.guest.is_alive()):
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if (not (self.queue.empty())) and table.guest is None:
                    table.guest = self.queue.get()
                    print(
                        f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    thread_temp = table.guest
                    thread_temp.start()
                    Cafe.threads_ls.append(thread_temp)


def main():
    tables = [Table(number) for number in range(1, 6)]
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    guests = [Guest(name) for name in guests_names]
    cafe = Cafe(*tables)
    cafe.guest_arrival(*guests)
    cafe.discuss_guests()

    for thr in Cafe.threads_ls:
        thr.join()


if __name__ == '__main__':
    main()
