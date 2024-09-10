# 2023/09/24 00:00|Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"

# Кортеж нельзя изменять без приведения в список и обратно.
immutable_var = (1, 5.2, 'string', [1, 2])
print(f'Кортеж - {immutable_var}')
immutable_var[3][0] = 5
print(f'Изменили знач. индекса [3] - {immutable_var}')
immutable_var = list(immutable_var)
immutable_var[0] = 'string'
immutable_var[2] = 1
immutable_var = tuple(immutable_var)
print(f'Поменяли местами знач. индексов [0] и [3] - {immutable_var}\n')

# Список (Массив) можно менять в любом порядке.
mutable_list = [1, 'a', 3.5]
print(f'Список - {mutable_list}')
mutable_list[0] = 'b'
mutable_list[1] = 5.7
mutable_list[2] = 3
print(f'Изменённый Список - {mutable_list}')
