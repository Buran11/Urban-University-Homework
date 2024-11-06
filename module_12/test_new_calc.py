import calc
import unittest


class NewCalcTest(unittest.TestCase):

    def test_sqrt(self):
        self.assertEqual(calc.sqrt(4), 2)

    def test_pow(self):
        self.assertEqual(calc.pow(3, 3), 27)


if __name__ == '__main__':
    unittest.main()
