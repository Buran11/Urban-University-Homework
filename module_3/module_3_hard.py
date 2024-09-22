# 2023/10/16 00:00|Дополнительное практическое задание по модулю*

def calculate_structure_sum(data_structure):
    sum_elements = 0
    if isinstance(data_structure, str):
        sum_elements += len(data_structure)
    elif isinstance(data_structure, int):
        sum_elements += data_structure
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            sum_elements += calculate_structure_sum(key)
            sum_elements += calculate_structure_sum(value)
    elif isinstance(data_structure, (list, tuple, set)):
        for i in data_structure:
            sum_elements += calculate_structure_sum(i)
    return sum_elements


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)

# 99
