#2023/10/06 00:00|Домашняя работа по уроку "Пространство имён"

calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), str.upper(string), str.lower(string)

def is_contains(string, list_to_search):
    count_calls()
    flag_is_contains = False
    str.lower(string)
    for i in list_to_search:
        i = str.lower(i)
        if i == str.lower(string):
            flag_is_contains = True
        else:
            flag_is_contains = False
    return flag_is_contains

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)