# 2023/12/04 00:00|Домашнее задание по теме "Генераторы"

def all_variants(text):
    '''
    Генератор всех возможных вариантов входной строки
    '''
    for i in range(len(text) + 1):
        for j in range(i):
            yield text[j:i]


def main():
    a = all_variants("abc")
    for i in a:
        print(i)


if __name__ == '__main__':
    main()
