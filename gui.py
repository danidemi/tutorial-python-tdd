from tkinter import *
from calctest import *

class NumberCall:
    def __init__(self, calc, digit):
        self.calc = calc
        self.digit = digit

    def __call__(self):
        print("call")
        print(self.calc)
        print(self.digit)
        self.calc.pressDigit(self.digit)
        return None

class Application(Frame):

    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets2(self):

        self.Display = Entry(self)
        self.Display.pack({"side": "left"})

        Operators = Frame(self)
        self.PlusBtn = Button(Operators)
        self.PlusBtn["text"] = "+"
        self.PlusBtn["command"] = self.pressPlus
        self.PlusBtn.pack({"side": "left"})
        self.MinusBtn = Button(Operators)
        self.MinusBtn["text"] = "-"
        self.MinusBtn["command"] = None
        self.MinusBtn.pack({"side": "left"})
        self.EqualsBtn = Button(Operators)
        self.EqualsBtn["text"] = "="
        self.EqualsBtn["command"] = self.pressEqual
        self.EqualsBtn.pack({"side": "left"})
        Operators.pack()

        Digits = Frame(self)
        self.DigitBtn = []
        for i in range(0,10):
            TheButton = Button(Digits, text=str(i))
            TheButton.pack(side=LEFT)
            self.DigitBtn = self.DigitBtn + [TheButton]
        Digits.pack()
        self.DigitBtn[0]["command"] = lambda: self.pressDigit(0)
        self.DigitBtn[1]["command"] = lambda: self.pressDigit(1)
        self.DigitBtn[2]["command"] = lambda: self.pressDigit(2)
        self.DigitBtn[3]["command"] = lambda: self.pressDigit(3)
        self.DigitBtn[4]["command"] = lambda: self.pressDigit(4)
        self.DigitBtn[5]["command"] = lambda: self.pressDigit(5)
        self.DigitBtn[6]["command"] = lambda: self.pressDigit(6)
        self.DigitBtn[7]["command"] = lambda: self.pressDigit(7)
        self.DigitBtn[8]["command"] = lambda: self.pressDigit(8)
        self.DigitBtn[9]["command"] = lambda: self.pressDigit(9)

    def update(self):
        self.Display.delete(0, END)
        self.Display.insert(0, self.calculator.display())
        print(self.calculator.display())

    def pressDigit(self, digit):
        self.calculator.pressDigit(digit)

    def pressPlus(self):
        self.calculator.pressPlus()

    def pressEqual(self):
        self.calculator.pressEquals()

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.calculator=Calculator()
        self.calculator.addObserver(self)
        self.pack()
        self.createWidgets2()


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
