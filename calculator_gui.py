from tkinter import *
from calculator_model import CalculatorModel

class CalculatorGUI(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.calculator=CalculatorModel()
        self.calculator.addObserver(self)
        self.pack()
        self._create_widgets()

    def _create_widgets(self):

        self.Display = Entry(self)
        self.Display.pack({"side": "left"})

        Operators = Frame(self)
        self.PlusBtn = Button(Operators)
        self.PlusBtn["text"] = "+"
        self.PlusBtn["command"] = self.press_plus
        self.PlusBtn.pack({"side": "left"})
        self.MinusBtn = Button(Operators)
        self.MinusBtn["text"] = "-"
        self.MinusBtn["command"] = None
        self.MinusBtn.pack({"side": "left"})
        self.EqualsBtn = Button(Operators)
        self.EqualsBtn["text"] = "="
        self.EqualsBtn["command"] = self.press_equal
        self.EqualsBtn.pack({"side": "left"})
        Operators.pack()

        Digits = Frame(self)
        self.DigitBtn = []
        for i in range(0,10):
            TheButton = Button(Digits, text=str(i))
            TheButton.pack(side=LEFT)
            self.DigitBtn = self.DigitBtn + [TheButton]
        Digits.pack()
        self.DigitBtn[0]["command"] = lambda: self.press_digit(0)
        self.DigitBtn[1]["command"] = lambda: self.press_digit(1)
        self.DigitBtn[2]["command"] = lambda: self.press_digit(2)
        self.DigitBtn[3]["command"] = lambda: self.press_digit(3)
        self.DigitBtn[4]["command"] = lambda: self.press_digit(4)
        self.DigitBtn[5]["command"] = lambda: self.press_digit(5)
        self.DigitBtn[6]["command"] = lambda: self.press_digit(6)
        self.DigitBtn[7]["command"] = lambda: self.press_digit(7)
        self.DigitBtn[8]["command"] = lambda: self.press_digit(8)
        self.DigitBtn[9]["command"] = lambda: self.press_digit(9)

    def update(self):
        self.Display.delete(0, END)
        self.Display.insert(0, self.calculator.display())
        print(self.calculator.display())

    def press_digit(self, digit):
        self.calculator.press_digit(digit)

    def press_plus(self):
        self.calculator.press_plus()

    def press_equal(self):
        self.calculator.press_equals()
