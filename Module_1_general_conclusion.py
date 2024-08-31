#2023/09/26 00:00|Шпаргалка по типам данных в языке программирования Python

#Числа
a = 5
print(f'Var: {a}, is of type: {type(a)}.')
a = 2.0
print(f'Var: {a}, is of type: {type(a)}.')
a = 1 + 2j
print(f'Var: {a}, is of complex number? {isinstance(a, complex)}\n')
#Списки
l = [1, 3, 5, 7, 7, 8]
print(type(l), l)
print(f'list_[2] = {l[2]}')
print(f'l[:3]: {l[:3]}')
print(f'l[5:]: {l[5:]}')
print(f'l[::-1]: {l[::-1]}\n')
#Кортежи
t = (1, 'Python', 5.5, 3+8j, [7, 8])
print(type(t), t)
print(f't[1]: {t[1]}')
print(f't[:3]: {t[:3]}')
#Строки
s = 'Hello World!'
print(s)
print(list(s))
print(s[0])
#Множества
s = {1, 2, 3, 4, 4, 4}
print(type(s), s)
#Словари
d = {1: 'Python', 'Int': 235}
print(type(d), d)
print(d[1])
print(d['Int'])
#Приведение
var = [1, 2, 3]
print(set(var))
print(tuple(var))
var = [[1, 2], [3, 4]]
print(dict(var))