import unittest
import inspect

class Calculator:

    def __init__(self):
        self._accumulator = 0
        self._current = 0

    def display(self):
        return str( self._current )

    def pressDigit(self, digit):
        self._current = digit

    def pressPlus(self):
        self._accumulator = self._current
        self._operator = lambda a,c: a+c

    def pressMinus(self):
        self._accumulator = self._current
        self._operator = lambda a,c: a-c

    def pressMult(self):
        self._accumulator = self._current
        self._operator = lambda a,c: a*c

    def pressEquals(self):
        self._current = self._operator(self._accumulator, self._current)


class TestCalc( unittest.TestCase ):

    def setUp(self):
        self.c = Calculator()

    def tearDown(self):
        self.c = None

    def test_work(self):
        print(self)

    def test_fail(self):
        self.assertTrue(not False)

    def testShouldShowZeroWhenInitialized(self):
        self.assertEqual("0", self.c.display())

    def testShouldReturnOneWhenOneIsPressed(self):
        self.c.pressDigit(1);
        self.assertEqual("1", self.c.display())

    def testShouldReturnTwoWhenOnePlusOne(self):
        self.c.pressDigit(1);
        self.assertEqual("1", self.c.display())

        self.c.pressPlus();
        self.assertEqual("1", self.c.display())

        self.c.pressDigit(1);
        self.assertEqual("1", self.c.display())

        self.c.pressEquals();
        self.assertEqual("2", self.c.display())

    def testMinus(self):
        self.c.pressMinus()
        self.c.pressDigit(1)
        self.c.pressEquals()
        self.assertEqual("-1", self.c.display())

    def testMult(self):
        self.c.pressDigit(2)
        self.c.pressMult()
        self.c.pressDigit(2)
        self.c.pressEquals()
        self.assertEqual("4", self.c.display(), "2*2=4")


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
