import unittest


def add_string(string_1, string_2):
    return string_1 + string_2


def add_integer(integer_1, integer_2):
    return integer_1 + integer_2


def comparision(foo, bar):
    return foo == bar


class FooncTest(unittest.TestCase):
    @staticmethod
    

    @staticmethod
    def tearDownClass(self):
        print('Megardown')

    def test_add_string(self):
        self.assertIsInstance(add_string('a', 'b'), str)

    def test_add_integer(self):
        self.assertIsInstance(add_integer(1, 2), int)

    def test_comparision(self):
        self.assertEqual(comparision(2, 2), False)


if __name__ == '__main__':
    unittest.main()
