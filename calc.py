from tkinter import Tk
from calculator_gui import CalculatorGUI

root = Tk()
app = CalculatorGUI(master=root)
app.mainloop()
root.destroy()
