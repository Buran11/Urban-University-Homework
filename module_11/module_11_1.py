# 2023/12/22 00:00|Домашнее задание по теме 'Обзор сторонних библиотек Python'
import PIL.Image
import requests
import pandas
import numpy
import matplotlib.pyplot as plt
import PIL  # pip install Pillow


# requests
def requests_controller():
    ref = requests.get('https://yandex.ru', verify=True)
    print(ref)
    print(ref.headers)
    ref.text


# pandas numpy
def pandas_numpy_controller():
    series = pandas.Series([1, 2, 3], index=['a', 'b', 'c'], dtype=numpy.uint8)
    print(series)
    print(series.index)
    print(series['b'])

    dataframe = pandas.DataFrame([[1, 'Ivan', 5.0], [2, 'Sergey', 4.3], [
        3, 'Dmitry', 4.5]], columns=['#', 'Name', 'Score'])
    print(dataframe)
    print(dataframe['Name'])

    csv_file = pandas.read_csv('CSV_file.csv')
    print(csv_file.head)
    csv_file.to_excel('EXEL_file.xlsx')
    xlsx_file = pandas.read_excel('EXEL_file.xlsx')
    print(xlsx_file.head(2))


# matplotlib
def matplotlib_controller():
    # К графикам столбцов и точкек
    # x = [5, 7, 8, 7, 2, 17, 2, 9,
    #      4, 11, 12, 9, 6]
    # y = [99, 86, 87, 88, 100, 86,
    #      103, 87, 94, 78, 77, 85, 86]

    # К радиальному графику
    cars = ['AUDI', 'BMW', 'FORD',
            'TESLA', 'JAGUAR', 'MERCEDES']
    data = [23, 17, 35, 29, 12, 41]

    # plt.scatter(x, y, c="blue") # График в виде точек
    # plt.bar(x, y) # График в виде столбцов
    plt.figure(figsize=(10, 7))  # Радиальный график
    plt.pie(data, labels=cars)
    plt.show()


# Pillow
def pillow_controller():
    jpg_file = 'panda.jpg'
    with PIL.Image.open(jpg_file) as img:
        img.load()
        img.show()
        cropped_img = img.crop((900, 800, 1600, 1500))
        cropped_img.size
        low_res_img = cropped_img.resize(
            (cropped_img.width // 1, cropped_img.height // 1))
        low_res_img.show()
        img.format
        img.size
        img.mode


def main():
    # requests_controller()
    # pandas_numpy_controller()
    # matplotlib_controller()
    pillow_controller()


if __name__ == '__main__':
    main()
