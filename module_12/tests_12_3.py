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


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, reason='Тесты в этом кейсе заморожены.')
    def test_walk(self):
        runner = Runner('Maria')
        for _ in range(10):
            runner.walk()
        self.assertEqual(50, runner.distance)

    @unittest.skipIf(is_frozen, reason='Тесты в этом кейсе заморожены.')
    def test_run(self):
        runner = Runner('Maxim')
        for _ in range(10):
            runner.run()
        self.assertEqual(100, runner.distance)
        # self.assertEqual(50, runner.distance)  # AssertionError

    @unittest.skipIf(is_frozen, reason='Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        runner1 = Runner('Alex')
        runner2 = Runner('Maxim')
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TurnamentTest(unittest.TestCase):
    is_frozen = True

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

    @unittest.skipIf(is_frozen, reason='Тесты в этом кейсе заморожены.')
    def test_start1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        self.all_results.update(tournament.start())
        last_key = max(self.all_results.keys())
        self.assertTrue(self.all_results.get(
            last_key).name == self.runner3.name)

    @unittest.skipIf(is_frozen, reason='Тесты в этом кейсе заморожены.')
    def test_start2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        self.all_results.update(tournament.start())
        last_key = max(self.all_results.keys())
        self.assertTrue(self.all_results.get(
            last_key).name == self.runner3.name)

    @unittest.skipIf(is_frozen, reason='Тесты в этом кейсе заморожены.')
    def test_start3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results.update(tournament.start())
        last_key = max(self.all_results.keys())
        self.assertTrue(self.all_results.get(
            last_key).name == self.runner3.name)


if __name__ == '__main__':
    unittest.main()
