import unittest
import unittest_demo


class UnitTestDemoTest(unittest.TestCase):

    def test_one(self):
        sample = "hello"
        result = unittest_demo.init_cap(sample)
        print(result)
        self.assertEqual(result, "Hello")

    def test_tow(self):
        sample = "hello World. This is python speaking."
        result = unittest_demo.init_cap(sample)
        print(result)
        self.assertEqual(result, "Hello World. This Is Python Speaking.")
