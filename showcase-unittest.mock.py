from unittest.mock import MagicMock
import unittest

class TestMock(unittest.TestCase):

    def test_Mock(self):
        sut = MyClass();
        sut.anInt = MagicMock(return_value=3)
        print(sut.anInt())

class MyClass():
    def anInt(self):
        return 5

if __name__ == '__main__':
    unittest.main()
