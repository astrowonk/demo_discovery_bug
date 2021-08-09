import unittest
from module_one.MyExample import MyExample


class MyExampleTest(unittest.TestCase):
    def test_example(self):
        t = MyExample()
        self.assertEqual(t.aMethod(1, 1), 2)
