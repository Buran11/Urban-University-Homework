# 2023/11/16 00:00|Домашнее задание по теме "Позиционирование в файле".

def custom_write(file_name: str, string: list):
    """
    Возвращает словарь с информацией о длине и количестве строк в файле.
    """
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(len(string)):
            keys = (i + 1, file.tell())
            file.write(string[i] + '\n')
            strings_positions[keys] = string[i]
        file.close()
    return strings_positions

# Вывод на консоль:
# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')


    # Точка входа
if __name__ == '__main__':
    # Пример выполняемого кода:
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!']

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
