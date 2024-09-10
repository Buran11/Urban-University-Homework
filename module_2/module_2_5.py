# 2023/10/03 00:00|Домашняя работа по уроку "Функции в Python.Функция с параметром"

def get_matrix(n=None, m=None, value=None):
    matrix = []
    temp_list = []
    flag = False
    row, col = range(0, n), range(0, m)
    if n <= 0 or m <= 0:
        flag = False
    else:
        for i in row:
            matrix.append(temp_list)
            for j in col:
                temp_list.append(value)
                break
        flag = True
    return matrix if flag else temp_list


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

# Тест на отрицательное и нулевое значение аргументов
result_test_exp1 = get_matrix(-1, 2, 3)
result_test_exp2 = get_matrix(0, 2, 3)
result_test_exp3 = get_matrix(3, -1, 3)
result_test_exp4 = get_matrix(3, 0, 3)
print(result_test_exp1, result_test_exp2, result_test_exp3, result_test_exp4)
