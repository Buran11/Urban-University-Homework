# 2023/12/15 00:00|Домашнее задание по теме "Многопроцессное программирование"
import multiprocessing
from datetime import datetime


def read_info(name: str):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            if len(line) == 0:
                break
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]


def liner():
    time_start = datetime.now()
    read_info(filenames[0])
    read_info(filenames[1])
    read_info(filenames[2])
    read_info(filenames[3])
    time_end = datetime.now()
    print(time_end - time_start, '(линейный)')


def multiprocess():
    time_start = datetime.now()
    proc1 = multiprocessing.Process(target=read_info, args=(filenames[0],))
    proc2 = multiprocessing.Process(target=read_info, args=(filenames[1],))
    proc3 = multiprocessing.Process(target=read_info, args=(filenames[2],))
    proc4 = multiprocessing.Process(target=read_info, args=(filenames[3],))
    proc1.start()
    proc2.start()
    proc3.start()
    proc4.start()
    proc1.join()
    proc2.join()
    proc3.join()
    proc4.join()
    time_end = datetime.now()
    print(time_end - time_start, '(многопроцессный)')


if __name__ == '__main__':
    liner()
    multiprocess()
