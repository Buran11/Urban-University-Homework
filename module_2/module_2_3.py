# 2023/10/01 00:00|Домашняя работа по уроку "Стиль кода часть II. Цикл While."

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count_index = 0
while_decision = (count_index <= len(my_list))

while while_decision:
    if my_list[count_index] > 0:
        print(my_list[count_index])
        count_index += 1
        continue
    elif my_list[count_index] == 0:
        count_index += 1
        continue
    else:
        break
