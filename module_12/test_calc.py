import calc
import unittest


class CalcTest(unittest.TestCase):
    def setUp(self):
        print('setup')

    @classmethod
    def setUpClass(cls):
        print('Megasetup')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_add(self):
        '''
        Test for ad function in calculator
        :return:
        '''
        self.assertEqual(calc.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(calc.sub(2, 1), 1)


if __name__ == '__main__':
    unittest.main()
