# 2023/11/05 00:00|Дополнительное практическое задание по модулю*

from time import sleep


class User:
    '''
    Класс, инициализирующий пользователя. 
    атрибуты:
    nickname - логин,
    password - пароль,
    age - возраст.
    '''

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    '''
    Класс, имитирующий видео-файл. 
    атрибуты:
    title - название,
    duration - продолжительность,
    time_now - текущее время,
    adult_mode - режим контроля PEGI.
    '''

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, other):
        return other in self.title


class UrTube:
    '''
    Класс осуществляет взаимодействие между пользователями и видео файлами.
    Методы класса:
    log_in - вход в аккаунт,
    register - регистрация,
    log_out - выход из аккаунта,
    add - добавление видео,
    get_videos - поиск видео,
    watch_video - просмотр видео.
    '''

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname and password == user.password:  # если пароль и логин совпадают
                self.current_user = user

    def register(self, nickname, password, age):
        password = hash(password)
        for user in self.users:
            if user.nickname == nickname:  # если пользователь уже существует
                print(f'Пользователь {nickname} уже существует')
                break
        self.users.append(User(nickname, password, age))
        self.current_user = User(nickname, password, age)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i in self.videos:  # если видео уже существует
                continue
            else:
                self.videos.append(i)

    def get_videos(self, serch_word):
        serch_word = str(serch_word)
        ls_videos = []
        for i in self.videos:
            if serch_word.casefold() in i.title.casefold():  # если название видео содержит введенное слово
                ls_videos.append(i.title)
        return ls_videos

    def watch_video(self, wath_video):
        wath_video = str(wath_video)
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for i in self.videos:
                if i.title == wath_video:  # если название видео совпадает
                    if i.adult_mode and self.current_user.age < 18:  # если режим контроля PEGI 18 соответствует
                        print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                        return
                    while i.time_now < i.duration:  # хронометраж видео
                        print(i.time_now + 1, end=' ')
                        # sleep(0.1) # тест для ускорения
                        sleep(1)
                        i.time_now += 1
                    print('Конец видео')
                    break


# Вывод в консоль:
# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist

# Точка входа
if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    # Добавление видео
    ur.add(v1, v2)
    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))
    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')
    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)
    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
