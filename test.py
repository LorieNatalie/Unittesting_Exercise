import unittest
import main

class TestMyTestcase(unittest.TestCase):

    def test_EvenNumbers(self):
        output=main.EvenNumbers([1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(output,[2,4,6,8,10])
        self.assertNotEqual(output,[4,6,8,10])

    def test_OddNumbers(self):
        output=main.OddNumbers([1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(output,[1,3,5,7,9])
        self.assertNotEqual(output,[3,5,7,9])