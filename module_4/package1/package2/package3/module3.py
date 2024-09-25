class verification:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __save(self):
        with open('data.txt', 'a') as file:
            file.write(f'{(self.name, self.password)}' + '\n')

    def check(self):
        with open('data.txt') as file:
            for line in file:
                if f'{self.name, self.password}' + '\n' == line:
                    raise ValueError('Такой пользователь уже существует')
                if len(self.password) < 8:
                    raise ValueError('Пароль слишком короткий')

            print('Пользователь успешно зарегистрирован')
            self.__save()
