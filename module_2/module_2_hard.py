# 2023/10/04 00:00|Дополнительное практическое задание по модулю*

import os

# Exception constantes
EXCEPTION_001 = f'TypeError_001: The type of data entered does not match\
 the "INT" type, entered number 27 to exit or next try again entering!!!'
EXCEPTION_002 = f'InputError_001: Incorrect input, enter a value in the\
 range from 3 to 20 or entered number 27 to exit!!!'

# Methods in app


def set_input_number():
    flag = True
    while flag:
        try:
            n = int(input('Введите цело число от 3 до 20: '))
            if n >= 3 and n <= 20:
                flag = False
                return n
            if n == 27:
                break
            else:
                print(EXCEPTION_002)
        except:
            print(EXCEPTION_001)


def get_generated_password(input_number):
    temp_list = []
    sum_index_values = 1
    count_nested_list = 0
    for i in range(1, input_number):
        count_nested_list += 1
        for j in range(count_nested_list, input_number):
            sum_index_values = i + j
            if input_number % sum_index_values == 0:
                if i != j:
                    temp_list.extend([i, j])
    return temp_list


def convert_list_to_str(List):
    string_values = ''
    for i in List:
        string_values += str(i)
    return string_values


def init():
    input_number = set_input_number()
    list_password = get_generated_password(input_number)
    string_password = convert_list_to_str(list_password)
    os.system('cls')
    print(f'{input_number} - {string_password}\n')


# Entery point
init()

# 3 - 12
# 4 - 13
# 5 - 1423
# 6 - 121524
# 9 - 1218273645
# 10 - 141923283746
# 11 - 11029384756
# 20 - 13141911923282183731746416515614713812911
