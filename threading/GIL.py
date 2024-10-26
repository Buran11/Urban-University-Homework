# GIL (Global Interpriter Lock) - глобальная блокировка интерпретатора
# x = 0
# for i in range(1000000):
#     x += 1

# I/O bound - операции ввода/вывода (Input/Output операции)
# GIL не блокирует всё, кроме тех операций, которые связанны с обработкой Python кода (пример: range(), list(), len(), etc.)

from threading import Thread


def count_up(name, n):
    for i in range(n):
        print(name, i, sep=': ')


t1 = Thread(target=count_up, args=('Thread1', 5))
t2 = Thread(target=count_up, args=('Thread2', 5))

t1.start()
t2.start()

t1.join()
t2.join()

# GIL меняет потоки для выполнения
# Thread1: 0
# Thread1: 1
# Thread2: 0
# Thread1: 2
# Thread2: 1
# Thread2: 2
# Thread1: 3
# Thread1: 4
# Thread2: 3
# Thread2: 4
