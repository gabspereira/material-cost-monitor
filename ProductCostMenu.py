from tkinter import *
from tkinter.filedialog import askopenfilename
import os
cwd = os.getcwd() + '/'


def NewFile():
    print("New File!")
def OpenFile():
    name = askopenfilename()
    print(name)
def About():
    print("This is a simple example of a menu")

def DataBaseCur():
    os.startfile(cwd + 'material-cost-monitor' + "/code/1.0-gfp-simaris-calculation-engine.py")
    print("LV FY20 Database running...")

def SummarizeCalc():
    os.startfile(cwd + 'material-cost-monitor' + "/code/01-lv-calculation-summary.py")
    print("Summarizing Calculation report...")

root = Tk()
root.title("SI-DS Product Cost Menu")
root.geometry("600x400")
menu = Menu(root)
root.config(menu=menu)

lv = Menu(menu)
menu.add_cascade(label="LV", menu=lv)
lv.add_command(label="Database [FY20]", command=DataBaseCur)
lv.add_command(label="Summarize Calculation", command=SummarizeCalc)

mainloop()
