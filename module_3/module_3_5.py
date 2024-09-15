# 2023/10/11 00:00|Самостоятельная работа по уроку "Рекурсия"

def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


# Пример результата выполнения программы:
result = get_multiplied_digits(40203)
print(result)
