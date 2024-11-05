# 2024/01/09 00:00|Домашнее задание по теме "Методы Юнит-тестирования"
import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1

        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TurnamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.all_results = {}
        self.ls = []

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    def tearDown(self):
        res = {}
        for key, value in self.all_results.items():
            res.update({key: value.name})
        print(res)

    @classmethod
    def tearDownClass(self):
        pass

    def test_start1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        self.all_results.update(tournament.start())
        last_key = max(self.all_results.keys())
        self.assertTrue(self.all_results.get(
            last_key).name == self.runner3.name)

    def test_start2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        self.all_results.update(tournament.start())
        last_key = max(self.all_results.keys())
        self.assertTrue(self.all_results.get(
            last_key).name == self.runner3.name)

    def test_start3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results.update(tournament.start())
        last_key = max(self.all_results.keys())
        self.assertTrue(self.all_results.get(
            last_key).name == self.runner3.name)
    # При показателе дистанции 6 Ник обгоняет Андрей.


'''
    Для корректной работы нужно переписать метод start в классе Tournament так, 
    что бы он сортировал объекты класса Runner по скорости и пройденной дистанции.
    При зменении скорости у объектов класса Runner не меняется порядок их сортировки.
    При сравнение в test_start3 если указать дистанцию 6 или меньше, Ник обгоняет Андрей.
    
'''
if __name__ == '__main__':
    unittest.main()
    # runner1 = Runner('Усэйн', 10)
    # runner2 = Runner('Андрей', 9)
    # runner3 = Runner('Ник', 3)
    # tournament = Tournament(6, runner1, runner2, runner3)
    # a = tournament.start()
    # print(a)
