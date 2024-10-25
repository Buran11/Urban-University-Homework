# 2023/12/09 00:00|Домашнее задание по теме "Создание потоков".
from datetime import datetime
from threading import Thread
from time import sleep


def write_words(word_count: int, file_name: str):
    '''
    Создает файл с указанным количеством строк
    '''
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i}" + '\n')
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


def serial_output():
    '''
    Создаёт последовательно 4 файла
    '''
    time_start = datetime.now()
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')
    time_end = datetime.now()
    print(time_end - time_start)


def streaming_output():
    '''
    Создаёт потоки 4 файла
    '''
    time_start = datetime.now()
    thr_one = Thread(target=write_words, args=(10, 'example5.txt'))
    thr_two = Thread(target=write_words, args=(30, 'example6.txt'))
    thr_three = Thread(target=write_words, args=(200, 'example8.txt'))
    thr_four = Thread(target=write_words, args=(100, 'example7.txt'))
    # start() - запуск потока
    thr_one.start()
    thr_two.start()
    thr_three.start()
    thr_four.start()
    # join() - ожидание завершения потока
    thr_one.join()
    thr_two.join()
    thr_three.join()
    thr_four.join()
    time_end = datetime.now()
    print(time_end - time_start)


def main():
    serial_output()
    streaming_output()

    # Вывод на консоль:
    # Завершилась запись в файл example1.txt
    # Завершилась запись в файл example2.txt
    # Завершилась запись в файл example3.txt
    # Завершилась запись в файл example4.txt
    # 0:00:37.082653
    # Завершилась запись в файл example5.txt
    # Завершилась запись в файл example6.txt
    # Завершилась запись в файл example7.txt
    # Завершилась запись в файл example8.txt
    # 0:00:21.684241


if __name__ == '__main__':
    main()
