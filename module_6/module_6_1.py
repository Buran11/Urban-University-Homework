# 2023/11/07 00:00|Домашнее задание по теме "Зачем нужно наследование"

class Animal:
    '''
    Базовый класс животного.
    Атрибуты:
    alive - живое ли животное
    fed - съедено ли животное
    name - название животного
    '''

    def __init__(self, name, alive: bool = True, fed: bool = False):
        self.alive = alive
        self.fed = fed
        self.name = name

    # (конвенция DRY)
    # def eat(self, food):
    #     if food.edible:
    #         print(f'{self.name} съел {food.name}')
    #         self.fed = True
    #     else:
    #         print(f'{self.name} не стал есть {food.name}')
    #         self.alive = False


class Plant:
    '''
    Базовый класс растения.
    Атрибуты:
    edible - съедобное ли растение
    name - название растения
    '''

    def __init__(self, name, edible: bool = False):
        self.edible = edible
        self.name = name


class Mammal(Animal):
    '''
    Класс травоядное животное
    Методы:
    eat() - определяет что именно съедает животное

    '''
    # (конвенция DRY)
    # pass

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Predator(Animal):
    '''
    Класс хищное животное
    Методы:
    eat() - определяет что именно съедает животное
    '''
    # (конвенция DRY)
    # pass

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Flower(Plant):
    '''
    Класс цветок - не съедобное
    '''
    pass


class Fruit(Plant):
    '''
    Класс фрукт - съедобное
    '''

    def __init__(self, edible):
        super().__init__(edible)
        self.edible = True

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
