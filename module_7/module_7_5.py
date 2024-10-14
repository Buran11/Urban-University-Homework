# 2023/11/19 00:00|Домашнее задание по теме "Файлы в операционной системе".

'''
Создайте новый проект или продолжите работу в текущем проекте.
    Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
    Примените os.path.join для формирования полного пути к файлам.
    Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
    Используйте os.path.getsize для получения размера файла.
    Используйте os.path.dirname для получения родительской директории файла.
'''

import os
import time


def main():
    directory = r'E:\Urban\rep\Urban-University-Homework\module_7\second'
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            filetime = os.path.getmtime(filepath)
            formatted_time = time.strftime(
                "%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            parent_dir = os.path.dirname(filepath)
            print(
                f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

# Пример возможного вывода:
# Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11, Родительская директория.


# Точка входа
if __name__ == '__main__':
    main()
