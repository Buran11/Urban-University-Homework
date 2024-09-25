from .package2 import module2


class add_user():
    name = input('Введите любую логин: ')
    password = input('Введите любой пароль: ')
    module2.except_verification(name, password)
