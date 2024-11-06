import calc
import unittest
import random


class CalcTest(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     pass

    # def setUp(self):
    #     pass

    # def tearDown(self):
    #     pass

    # @classmethod
    # def tearDownClass(cls):
    #     pass

    @unittest.skip("demonstrating skipping")
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)

    @unittest.skipIf(random.randint(0, 2), "demonstrating skipping")
    def test_sub(self):
        self.assertEqual(calc.sub(2, 1), 1)

    def test_mul(self):
        self.assertEqual(calc.mul(1, 2), 2)

    def test_div(self):
        self.assertEqual(calc.div(1, 2), 0.5)


if __name__ == '__main__':
    unittest.main()
