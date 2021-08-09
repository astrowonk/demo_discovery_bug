import unittest
from module_two.MyExampleTwo import MyExampleTwo


class MyExampleTest(unittest.TestCase):
    def test_example(self):
        t = MyExampleTwo()
        self.assertEqual(t.aMethod(1, 1), 1)
