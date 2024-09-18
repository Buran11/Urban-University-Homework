# 2023/10/14 00:00|Практика по функциям

list_ = [1, 5, 6, 3, 8, 3, 5, 9, 2, 6,]


def find_max(list_):
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_


def count_even(list_):
    count = 0
    for i in list_:
        if i % 2 == 0:
            count += 1
    return count


def unique_list(list_):
    unique_list = []
    for i in list_:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


print(find_max(list_))
print(count_even(list_))
print(find_max(list_))
