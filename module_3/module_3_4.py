# 2023/10/10 00:00|Самостоятельная работа по уроку "Произвольное число параметров".

def single_root_words(root_word, *other_words):
    same_words = []
    root_word = str(root_word)
    for i in other_words:
        i = str(i)
        # if (root_word.casefold() in i.casefold()) or (i.casefold() in root_word.casefold()):
        if (root_word.lower() in i.lower()) or (i.lower() in root_word.lower()):
            same_words.append(i)
    return same_words


# Пример результата выполнения программы:
result1 = single_root_words(
    'rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
