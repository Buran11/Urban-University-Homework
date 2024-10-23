def null_decorator(func):
    def wrapper():
        origin_result = func()
        new_result = origin_result.upper()
        return new_result
    return wrapper


@null_decorator
def say_hallo():
    return 'hello'


a = say_hallo()
print(a)
