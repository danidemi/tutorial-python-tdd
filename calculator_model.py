class CalculatorModel:

    def __init__(self):
        self._accumulator = 0
        self._current = 0
        self._newOp = False
        self.observers = []

    def addObserver(self, observer):
        self.observers = self.observers + [observer]

    def _update(self):
        for observer in self.observers:
            observer.update()

    def display(self):
        return str( self._current )

    def press_digit(self, digit):

        try:
            theDigit = int(digit)
        except Exception as e:
            raise CalcError(str(digit) + " not an int")

        if(not theDigit in range(0,10)):
            raise CalcError(str(digit) + " not in 0..9 range")

        if(self._newOp):
            self._current = theDigit
            self._newOp = False
        else:
            self._current = self._current * 10 + theDigit

        self._update()


    def press_plus(self):
        self._accumulator = self._current
        self._operator = lambda a,c: a+c
        self._newOp = True

        self._update()

    def press_minus(self):
        self._accumulator = self._current
        self._operator = lambda a,c: a-c
        self._newOp = True

        self._update()

    def press_mult(self):
        self._accumulator = self._current
        self._operator = lambda a,c: a*c
        self._newOp = True

        self._update()

    def press_equals(self):
        self._current = self._operator(self._accumulator, self._current)

        self._update()

class CalcError(Exception):
    def __init__(self, text):
        self.value = text

    def __str__(self):
        return self.value
