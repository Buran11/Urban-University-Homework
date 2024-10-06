class Human:
    head = True

    def say_hallo(self):
        print('Hallo!')


class Student(Human):
    head = False

    def about(self):
        print('I am a student')


class Teacher(Human):
    pass


# human = Human()
student = Student()
teacher = Teacher()
student.say_hallo()
teacher.say_hallo()
print(student.head)
