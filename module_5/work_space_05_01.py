class Human:

    head = True
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

    def __str__(self):  # магический метод перегрузка str
        return f'Name: {self.name}'

    def __len__(self):
        return self.age

    def __lt__(self, other):  # магический метод сравнения перегрузка Lower than
        return self.age < other.age

    def __gt__(self, other):  # магический метод сравнения перегрузка Greater than
        return self.age > other.age

    def __eq__(self, other):  # магический метод сравнения перегрузка Equal to
        return self.age == other.age and self.name == other.name

    def __bool__(self):  # магический метод перегрузка bool
        return bool(self.age)

    def __del__(self):  # деструктор
        print(f'Good bye {self.name}')


den = Human('Denis', 22)  # экземпляр класса
max = Human('Maxim', 22)
a = 6
print(Human.head)

# print(den)  # str
# max.name = 'Denis'
# if den: # bool
#     den.say_info()
# print(den < max)  # False lt
# del den # удаление экземпляра
# max.birthday()
# print(len(den)) # возвращаем количество лет
# print(den < max)  # сравнение возраста True lt
# print(den > max)  # gt
# print(den == max)  # eq
# den.say_info()
# max.say_info()
# den.age += 1
# print(den.name, den.age)
# print(max.name, max.age)

if __name__ == '__main__':
    pass
