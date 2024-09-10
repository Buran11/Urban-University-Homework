# 2023/09/29 00:00|Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."

print('ЗАДАЧА: ВСЕ ЛИ РАВНЫ?')
print('Введите 3 целых числа.\n')
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second == third:
    print(3)
elif first == second or first == third or third == second:
    print(2)
else:
    print(0)
