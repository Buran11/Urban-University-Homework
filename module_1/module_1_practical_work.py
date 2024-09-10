# 2023/09/27 00:00|Дополнительное практическое задание по модулю*

# Input data
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [
    4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

# Exception constantes
EXCEPTION_001 = 'TypeError_001: convert_and_sort_set_object(set_)\
 - Argument type is not "Set" available!'
EXCEPTION_002 = 'TypeError_002: get_arithmetic_mean_in_list_values()\
 - The value of the argument must have a nested list!\n\
Example: list_ = [[1, 2], [3, 4]]'

# Methods in app


def convert_and_sort_set_object(set_=None):
    if (set_ != None) and (type(set_) == set):
        set_ = list(set_)
        set_.sort()
        return set_
    else:
        return print(EXCEPTION_001)


def get_arithmetic_mean_in_list_values(list_=None):
    output_res = []
    if (list_ != None) and (type(list_) == list):
        for i in list_:
            if type(i) == list:
                arithmetic_mean = (sum(i))/len(i)
                output_res.append(arithmetic_mean)
            else:
                print(EXCEPTION_002)
                break
    else:
        print(EXCEPTION_002)
    return output_res


def get_dict_db(key_list=None, value_list=None):
    res_dict = {}
    count = 0
    if type(key_list) == list and type(value_list) == list:
        if (len(key_list) == len(value_list)):
            for i in key_list:
                res_dict.update({key_list[count]: value_list[count]})
                count += 1
    return res_dict


def init():
    print(
        get_dict_db(
            convert_and_sort_set_object(students),
            get_arithmetic_mean_in_list_values(grades)))


# Entery point
init()
