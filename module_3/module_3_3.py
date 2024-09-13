# 2023/10/09 00:00|Самостоятельная работа по уроку "Распаковка позиционных параметров".

values_list = ['list', False, 2]
values_list_2 = [54.32, 'string']
values_dict = {'a': 'dict', 'b': False, 'c': 2}


def print_params(a=1, b='string', c=True):
    print(a, b, c)


# 1.Функция с параметрами по умолчанию:
print('**********')
print_params(1, 'string', True)
print_params()
print_params(25)
print_params([1, 2, 3])
print('**********')
# 2.Распаковка параметров:
print_params(*values_list)
print_params(**values_dict)
print('**********')
# 3.Распаковка + отдельные параметры:
print_params(*values_list_2, 42)
print('**********')
