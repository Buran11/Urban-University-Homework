# 2023/12/26 00:00|Домашнее задание по теме "Интроспекция"
class Introspectable:
    '''
    Возвращает словарь с данными об объекте, включающий следующую информацию:
    1 - Type: Тип объекта.
    2 - Atributs: Атрибуты объекта.
    3 - Methods: Методы объекта.
    4 - Modules: Модуль, к которому объект принадлежит.    
    '''

    def __init__(self, object: object):
        self.object = object
        self.__resalt = {}
        self.__introspection_info()

    def __introspection_info(self):
        from pprint import pprint
        type_ = type(self.object)
        atribut = dir(self.object)
        method = dir(type_)
        module = type_.__module__
        self.__resalt = {'1 - Type': type_, '2 - Atributs': atribut,
                         '3 - Methods': method, '4 - Modules': module}
        pprint(self.__resalt)


def main():
    Introspectable(1)


if __name__ == '__main__':
    main()
