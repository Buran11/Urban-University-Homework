# 2023/12/26 00:00|Домашнее задание по теме "Интроспекция"
import inspect


def introspection_info(obj: object):
    atributs = []
    methods = []
    type_ = type(obj)
    print(type_)
    for atribut in dir(obj):
        if not callable(getattr(obj, atribut)):
            atributs.append(atribut)
    for method in dir(obj):
        if callable(getattr(obj, method)):
            methods.append(method)
    module = inspect.getmodule(obj)
    resalt = {'1 - Type': type_, '2 - Atributs': atributs,
              '3 - Methods': methods, '4 - Module': module}
    print(resalt)


introspection_info(42)
