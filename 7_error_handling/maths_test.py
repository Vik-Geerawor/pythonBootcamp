import unittest
import maths


# inherits from TestCase
class TestMaths(unittest.TestCase):

    def test_add(self):
        result = maths.add(2, 3)
        self.assertEqual(result, 5)
