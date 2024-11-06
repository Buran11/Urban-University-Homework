# 2024/01/08 00:00|Домашнее задание по теме "Простые Юнит-Тесты"
import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5
        # self.distance += 10  # AssertionError

    def __str__(self):
        return self.name


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


if __name__ == '__main__':
    unittest.main()
