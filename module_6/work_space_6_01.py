class Human:
    head = True
    _legs = True
    __arms = True

    def say_hallo(self):
        print('Hallo!')

    def about(self):
        print(self.head, self._legs, self.__arms)


class Student(Human):
    arms = False
    pass


class Teacher(Human):
    pass


human = Human()
student = Student()


print(student._Human__arms)
