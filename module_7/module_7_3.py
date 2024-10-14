# 2023/11/17 00:00|Домашнее задание по теме "Оператор "with".

# import logging # для логирования


class WordsFinder():
    def __init__(self, *files):
        self.files = files
        self.files_name = self.files
        # logging.info('Файлы были перезаписанны в кортеж = self.files_name')

    def get_all_words(self):
        all_words = {}
        punctuation_marks = ',', '.', '=', '!', '?', ';', ':', ' - '
        for file in self.files:
            with open(file, 'r', encoding='utf-8') as line:
                for word in line.read().lower().split():
                    for mark in punctuation_marks:
                        word = word.replace(mark, '')
                    if word == '':
                        continue
                    all_words[file] = all_words.get(file, []) + [word]
        # logging.info('Слова из %s были получены = %s',
                    #  self.files_name, all_words)
        return all_words

    def find(self, word_in: str):
        count = 0
        for name, words in self.get_all_words().items():
            for word in words:
                if word_in.lower() != word.lower():
                    count += 1
                else:
                    count += 1
                    # logging.info('Слово "%s" по счёту "%s"',
                    #  word_in, count)
                    return {name: count}

    def count(self, word_in):
        count = 0
        for name, words in self.get_all_words().items():
            for word in words:
                if word_in.lower() == word.lower():
                    count += 1
            # logging.info('Слова "%s" в тексте всего "%s"',
                    #  word_in, count)
            return {name: count}


# Точка входа
if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO, filename='module_7_logs.log', filemode='w',
    #                     format='%(asctime)s %(levelname)s %(message)s', encoding='utf-8')

    # Пример выполнения программы:
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

    # Пример выполнения программы из доп. материалов к ТЗ:
    # finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
    # print(finder1.get_all_words()) # Все слова
    # print(finder1.find('Child')) # 2 слово по счёту
    # print(finder1.count('Child')) # 8 слова Child в тексте всего
