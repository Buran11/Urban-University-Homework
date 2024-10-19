# 2023/12/01 00:00|Домашнее задание по теме "Генераторные сборки"

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [len(i[0]) - len(i[1])
                for i in zip(first, second) if len(i[0]) != len(i[1])]
second_result = [False if len(first[i]) != len(
    second[i]) else True for i in range(len(first)) if len(first) == len(second)]


def main():
    print(list(first_result))
    print(list(second_result))


if __name__ == '__main__':
    main()
