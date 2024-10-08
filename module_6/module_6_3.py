# 2023/11/09 00:00|Домашнее задание по теме "Множественное наследование"

class Horse:
    '''Класс описывает лошадь'''
    x_distance = 0
    sound = 'Frrr'

    def __init__(self):
        super().__init__()
        self.sound = super().sound

    def run(self, dx: int):
        self.x_distance += dx


class Eagle:
    '''Класс описывает орла'''
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy: int):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    '''Класс описывает пегаса'''

    def __init__(self):
        super().__init__()
        self.x_distance = super().x_distance
        self.y_distance = super().y_distance

    def move(self, dx: int, dy: int):
        return (super().run(dx), super().fly(dy))

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)

# Вывод на консоль:
# (0, 0)
# (10, 15)
# (5, 35)
# I train, eat, sleep, and repeat


# Точка входа
if __name__ == '__main__':
    # print(Pegasus.mro())
    p1 = Pegasus()

    print(p1.get_pos())
    p1.move(10, 15)
    print(p1.get_pos())
    p1.move(-5, 20)
    print(p1.get_pos())

    p1.voice()
