class Human:
    # Метод вызывается при создании экземпляра. __init__ - магический метод, дандер метод
    def __init__(self, name, age) -> None:
        self.name = name  # Атрибут Переменные экземпляра
        self.age = age
        self.say_info()

    def say_info(self):
        print(f'Hi, my name is {self.name} and I am {self.age} years old')

    def birthday(self):
        self.age += 1
        print(f'Happy birthday {self.name}! You are {self.age} years old')

    def __len__(self):
        return self.age

    def __del__(self):  # деструктор
        print(f'Good bye {self.name}')


den = Human('Denis', 22)  # экземпляр класса
max = Human('Maxim', 22)
# del den # удаление экземпляра
max.birthday()
print(len(den))

# den.say_info()
# max.say_info()
# den.age += 1
# print(den.name, den.age)
# print(max.name, max.age)

if __name__ == '__main__':
    pass
