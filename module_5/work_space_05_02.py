class User:
    __instance = None

    def __new__(cls, *args, **kwargs):
        print('Я в new')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        print('Я в init')
        self.args = args
        self.kwargs = kwargs
        for key, values in kwargs.items():
            setattr(self, key, values)


other = [1, 2, 3]
user = {'name': 'Den', 'age': 25, 'gender': 'male'}

user1 = User(*other, **user)
print(user1.args)
print(user1.kwargs)
print(user1.name)
print(user1.age)
print(user1.gender)
