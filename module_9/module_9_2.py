# 2023/11/30 00:00|Домашнее задание по теме "Списковые, словарные сборки"

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension',
                  'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) > 5]
second_result = [
    (x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
third_result = [{x: len(x)} for x in first_strings if len(
    x) % 2 == 0] + [{x: len(x)} for x in second_strings if len(x) % 2 == 0]


def main():
    print(first_result)
    print(second_result)
    print(third_result)


# Точка входа
if __name__ == '__main__':
    main()
