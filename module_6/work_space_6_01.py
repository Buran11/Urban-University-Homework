class Human:
    def __init__(self, name, group):
        self.name = name
        super().__init__(group)
        super().about()

    def info(self):
        print(f'Hi, my name is {self.name}')


class StudentGroup:
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} is group {self.group}')


class Student(Human, StudentGroup):
    def __init__(self, name, place, group):
        super().__init__(name, group)
        self.place = place
        super().info()


# human = Human('Denis')
# print(human.name)
student = Student('Maxim', 'Urban', 'Python 1')

print(Student.mro())
