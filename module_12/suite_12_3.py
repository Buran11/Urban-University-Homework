# 2024/01/11 00:00|Домашнее задание по теме "Систематизация и пропуск тестов".
import unittest
import tests_12_1
import tests_12_2

module12ST = unittest.TestSuite()

module12ST.addTest(unittest.TestLoader(
).loadTestsFromTestCase(tests_12_1.RunnerTest))
module12ST.addTest(unittest.TestLoader(
).loadTestsFromTestCase(tests_12_2.TurnamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(module12ST)
