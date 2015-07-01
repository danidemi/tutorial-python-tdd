from unittest.mock import MagicMock
from unittest.mock import patch
import unittest
import sys

class MyClass():
    def anInt(self):
        return 5

class TestMock(unittest.TestCase):

    def test_redefine_method(self):
        sut = MyClass()
        sut.anInt = MagicMock(return_value=3)
        print(sut.anInt())

    def test_raise_exception(self):
        sut = MagicMock(side_effect=KeyError("oh!"))
        sut()

    def test_mock_method_to_raise_exception(self):
        sut = MyClass()
        sut.anInt = MagicMock(side_effect=KeyError("oh!"))
        print(sut.anInt())

    @patch('showcase-unittest.mock.MyClass')
    def test(self, MockedMyClass):
        print(globals())
        m = MockedMyClass()
        assert m is MyClass
        assert m.called



print(" >>>>>>>>>>>>>>>>>>>>>>>>>> " + str(sys.modules[ __name__]))
if __name__ == '__main__':
    unittest.main()
