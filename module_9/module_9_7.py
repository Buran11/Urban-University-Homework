# 2023/12/05 00:00|Домашнее задание по теме "Декораторы"

def is_prime(func):
    '''
    Декоратор для проверки на простое число
    '''
    def wrapper(*args):
        temp_resalt = func(*args)
        for i in range(2, temp_resalt):
            if i < 2:
                continue
            if temp_resalt % i == 0:
                print('Составное')
                break
            else:
                print('Простое')
                break
        return temp_resalt
    return wrapper


@is_prime
def sum_three(a, b, c):
    '''
    Сумма трех чисел
    '''
    return a + b + c


def main():
    result = sum_three(2, 3, 6)  # Проверка на простое
    print(result)
    result = sum_three(2, 1, 3)  # Проверка на составное
    print(result)


if __name__ == '__main__':
    main()
