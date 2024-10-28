from threading import Thread, Event
import time


def first_worker():
    print('Первый рабочий приступил к своей задаче')
    event.wait()
    print('Первый рабочий продолжил выполнять свою задачу')
    time.sleep(5)
    print('Первый рабочий завершил свою задачу')


def second_worker():
    print('Второй рабочий приступил к своей задаче')
    time.sleep(10)
    print('Второй рабочий завершил свою задачу')
    event.set()


event = Event()
event.set()
event.clear()
print(event.is_set())
t1 = Thread(target=first_worker)
t2 = Thread(target=second_worker)
t1.start()
t2.start()
