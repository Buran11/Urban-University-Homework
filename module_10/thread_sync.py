from threading import Thread
import queue  # потокобезопасная очередь
from time import sleep


def producer(queue):
    c = 0
    while c < 10:
        c += 1
        message = 'ping' + str(c)
        queue.put(message)  # пишем в очередь


def worker(queue):
    c = 0
    while c < 10:
        c += 1
        message = queue.get()  # читаем из очереди
        sleep(1)
        print(message)


def consumer(queue):
    pass


q = queue.Queue()
tr1 = Thread(target=producer, args=(q, ))
tr2 = Thread(target=worker, args=(q, ))
tr1.start()
tr2.start()
tr1.join()
tr2.join()
