import unittest
import inspect

class Calculator:

    def __init__(self):
        self._accumulator = 0
        self._current = 0

    def display(self):
        return str( self._current )

    def pressOne(self):
        self._current = 1

    def pressPlus(self):
        self._accumulator = self._current
        self._operator = lambda x,y: x+y

    def pressMinus(self):
        self._accumulator = self._current
        self._operator = lambda x,y: x-y

    def pressEquals(self):
        self._current = self._operator(self._accumulator, self._current)

    def opPlus(a,b):
        return a + b;

    def opMinus(a,b):
        return a - b;


class TestCalc( unittest.TestCase ):

    def test_work(self):
        print(self)

    def test_fail(self):
        self.assertTrue(not False)

    def testShouldShowZeroWhenInitialized(self):
        c = Calculator()
        self.assertEqual("0", c.display())

    def testShouldReturnOneWhenOneIsPressed(self):
        c = Calculator()
        c.pressOne();
        self.assertEqual("1", c.display())

    def testShouldReturnTwoWhenOnePlusOne(self):
        c = Calculator()

        c.pressOne();
        self.assertEqual("1", c.display())

        c.pressPlus();
        self.assertEqual("1", c.display())

        c.pressOne();
        self.assertEqual("1", c.display())

        c.pressEquals();
        self.assertEqual("2", c.display())

    def testMinus(self):
        c = Calculator()

        c.pressMinus();
        c.pressOne();
        c.pressEquals();
        self.assertEqual("-1", c.display())


t = TestCalc()
if __name__ == '__main__':
    unittest.main()


## just prints info on unittest.TestCase
t = unittest.TestCase
m = inspect.getmembers(t)
s = ""
for m1 in m:
    s = s + str(m1) + "\n"

print(s)
