import unittest
import inspect
from calculator_model import CalculatorModel, CalcError


class TestCalc( unittest.TestCase ):

    def setUp(self):
        self.c = CalculatorModel()

    def tearDown(self):
        self.c = None

    def test_work(self):
        print(self)

    def test_fail(self):
        self.assertTrue(not False)

    def testShouldShowZeroWhenInitialized(self):
        self.assertEqual("0", self.c.display())

    def testShouldReturnOneWhenOneIsPressed(self):
        self.c.press_digit(1);
        self.assertEqual("1", self.c.display())

    def testShouldReturnTwoWhenOnePlusOne(self):
        self.c.press_digit(1);
        self.assertEqual("1", self.c.display())

        self.c.press_plus();
        self.assertEqual("1", self.c.display())

        self.c.press_digit(1);
        self.assertEqual("1", self.c.display())

        self.c.press_equals();
        self.assertEqual("2", self.c.display())

    def testMinus(self):
        self.c.press_minus()
        self.c.press_digit(1)
        self.c.press_equals()
        self.assertEqual("-1", self.c.display())

    def testMult(self):
        self.c.press_digit(2)
        self.c.press_mult()
        self.c.press_digit(2)
        self.c.press_equals()
        self.assertEqual("4", self.c.display(), "2*2=4")

    def testShouldRefuseStrings(self):
        self.assertRaises(CalcError, self.c.press_digit, "aas")

    def testShouldRefuseMoreThanOneDigit(self):
        self.assertRaises(CalcError, self.c.press_digit, 99)


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
