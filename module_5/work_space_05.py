class Human:
    def __init__(self, name, age) -> None:  # Метод вызывается при создании экземпляра
        self.name = name  # Атрибут Переменные экземпляра
        self.age = age
        self.say_info()

    def say_info(self):
        print(f'Hi, my name is {self.name} and I am {self.age} years old')

    def birthday(self):
        self.age += 1
        print(f'Happy birthday {self.name}! You are {self.age} years old')


den = Human('Denis', 22)  # экземпляр класса
max = Human('Maxim', 22)
max.birthday()

# den.say_info()
# max.say_info()
# den.age += 1
# print(den.name, den.age)
# print(max.name, max.age)
