from tkinter import *

class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets2(self):

        self.Display = Entry(self)
        self.Display.pack({"side": "left"})

        Operators = Frame(self)
        self.PlusBtn = Button(Operators)
        self.PlusBtn["text"] = "+"
        self.PlusBtn["command"] = None
        self.PlusBtn.pack({"side": "left"})
        self.MinusBtn = Button(Operators)
        self.MinusBtn["text"] = "-"
        self.MinusBtn["command"] = None
        self.MinusBtn.pack({"side": "left"})
        self.EqualsBtn = Button(Operators)
        self.EqualsBtn["text"] = "="
        self.EqualsBtn["command"] = None
        self.EqualsBtn.pack({"side": "left"})
        Operators.pack()

        Digits = Frame(self)
        self.DigitBtn = []
        for i in range(0,10):
            TheButton = Button(Digits)
            TheButton["text"] = i
            TheButton["command"] = None
            TheButton.pack({"side": "left"})
            self.DigitBtn = self.DigitBtn + [TheButton]
        Digits.pack()




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
        self.pack()
        self.createWidgets2()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
