# 2023/10/08 00:00|Домашняя работа по уроку "Способы вызова функции"
import os


def set_exception_printed(exception_case, recipient=None, sender=None, ):
    if exception_case == 1:
        print(f'Невозможно отправить письмо с адреса',
              f'{recipient} на адрес {sender}')
    elif exception_case == 2:
        print('Нельзя отправить письмо самому себе!')
    elif exception_case == 3:
        print(f'Письмо успешно отправлено с адреса',
              f'{sender} на адрес {recipient}.')
    elif exception_case == 4:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса',
              f'{sender} на адрес {recipient}.')
    else:
        print('Не указан номер исключения (1, 2, 3 или 4)')


def send_email(message, recipient, sender='university.help@gmail.com'):
    recipient = str(recipient)
    str_ = recipient + sender
    tuple_ = ('.com', '.net', '.ru')
    if '@' not in str_ or not sender.endswith(tuple_) or not recipient.endswith(tuple_):
        set_exception_printed(1, recipient, sender)
    elif sender == recipient:
        set_exception_printed(2, recipient, sender)
    elif sender == 'university.help@gmail.com':
        set_exception_printed(3, recipient, sender)
    else:
        set_exception_printed(4, recipient, sender)


# Пример выполняемого кода (тесты):
os.system('cls')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание',
           'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре',
           'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
