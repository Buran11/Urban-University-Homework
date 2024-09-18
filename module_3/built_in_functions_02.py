# 2023/10/13 00:00|Встроенные функции. Часть 2

a = [True, False, False]
b = [0, 0, 0]
# any - есть хотя бы один True, all - все True
print(any(a), any(b), all(a), all(b))
c = [1, 1, 1]
d = ''
# print(dir(c))
print(type(d))  # Тип объекта
# Проверяет является ли объект экземпляром данного типа
print(isinstance(d, str))
print(id(b), id(c))  # Отображает ячейку памяти, в которой находится объект
print(help(print))  # Отображает справку по данной функции


def helper():
    """
    Отображает справку по данной функции
    """
    pass


print(help(helper))
print(print.__doc__)  # Отображает справку по данной функции
