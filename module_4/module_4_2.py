def test_function():
    # global inner_function # (без return)Не работает
    def inner_function():
        print('Я в области видимости функции test_function')
    return inner_function


# Использовал замыкание
inner_function = test_function()
inner_function()
