# 2023/11/07 00:00|Домашнее задание по теме "Зачем нужно наследование"

class Animal:
    '''
    Базовый класс животного.
    Атрибуты:
    alive - живое ли животное
    fed - голодное ли животное
    name - название животного
    '''
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    '''
    Базовый класс растения.
    Атрибуты:
    edible - съедобное ли растение
    name - название растения
    '''
    edible = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    '''
    Класс травоядное животное
    '''
    pass


class Predator(Animal):
    '''
    Класс хищное животное    
    '''
    pass


class Flower(Plant):
    '''
    Класс цветок - не съедобное
    '''
    pass


class Fruit(Plant):
    '''
    Класс фрукт - съедобное
    '''

    edible = True

# Вывод на консоль:
# Волк с Уолл-Стрит
# Цветик семицветик
# True
# False
# Волк с Уолл-Стрит не стал есть Цветик семицветик
# Хатико съел Заводной апельсин
# False
# True


# Точка входа
if __name__ == '__main__':
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')
    print(a1.name)
    print(p1.name)
    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)
