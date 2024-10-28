from queue import Queue
import time
import threading

# q = Queue()  # очередь с максимальным размером (maxsize=10) FIFO
# q.put(5)  # добавляем элемент в очередь
# print(q.get(timeout=2))  # извлекаем элемент с задержкой
# print('Конец очереди')


def getter(queue):
    # while not queue.empty():
    #     item = queue.get()
    while True:
        time.sleep(5)
        item = queue.get()
        print(threading.current_thread(), ' взял элемент ', item)


q = Queue(maxsize=10)
thread1 = threading.Thread(target=getter, args=(q,))
thread1.start()

for i in range(10):
    time.sleep(2)
    q.put(i)
    print(threading.current_thread(), ' положил в очередь элемент ', i)
