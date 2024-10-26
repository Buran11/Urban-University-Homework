# 2023/12/11 00:00|Домашнее задание по теме "Блокировки и обработка ошибок"
from threading import Thread, Lock
import threading
from random import randint
from time import sleep


class Bank(Thread):
    '''
    Класс банк. Содержит методы для пополнения и снятия денежных средств
    '''

    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        tranzaction_add_balance = 100
        for i in range(tranzaction_add_balance):
            random_number = randint(50, 500)
            if self.balance >= 500 and self.lock.acquire():
                self.lock.release()
            else:
                self.balance += random_number
                print(f'Пополнение: {random_number}. Баланс: {self.balance}')
                sleep(0.01)

    def take(self):
        tranzaction_take_balance = 100
        for i in range(tranzaction_take_balance):
            random_number = randint(50, 500)
            if random_number > self.balance:
                print('Запрос отклонён, недостаточно средств!')
                self.lock.locked()
                break
            else:
                self.balance -= random_number
                print(f'Снятие: {random_number}. Баланс: {self.balance}')
                sleep(0.01)

    def run(self):
        pass


def main():
    bk = Bank()

    # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')


if __name__ == '__main__':
    main()
