# 2023/12/05 00:00|Домашнее задание по теме "Декораторы"

def is_prime(func):
    '''
    декоратор для проверки на простое число
    '''
    def wrapper(*args):
        for a in args:
            if a < 2:
                print('Составное')
                return False
            for i in range(2, int(a ** 0.5) + 1):
                if a % i == 0:
                    print('Составное')
                    return False
            print('Простое')
            return func(*args)
    return wrapper


@is_prime
def sum_three(a, b, c):
    '''
    сумма трех чисел
    '''
    return a + b + c


def main():
    result = sum_three(2, 3, 6)
    print(result)


if __name__ == '__main__':
    main()
