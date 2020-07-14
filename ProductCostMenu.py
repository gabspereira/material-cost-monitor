from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os
cwd = os.getcwd() + '/'
print(cwd)

def DataBaseCur():
    os.startfile(cwd + "/code/1.0-gfp-simaris-calculation-engine.py")
    print("LV FY20 Database running...")

def SummarizeCalc():
    os.startfile(cwd + "/code/01-lv-calculation-summary.py")
    print("Summarizing Calculation report...")

def Simaris_2_1():
    os.startfile("C:/Program Files/SIEMENS/SIMARIS configuration/2.1/SIMARISconfiguration.exe")
    print("Openning Simaris 2.1...")

def Simaris_2_3_18_19():
    os.startfile("C:/Program Files/SIEMENS/SIMARIS configuration/2.3 FY18-19/SIMARISconfiguration.exe")
    print("Openning Simaris 2.3 FY18-19...")

def Simaris_2_3_19_20():
    os.startfile("C:/Program Files/SIEMENS/SIMARIS configuration/2.3 FY19-20/SIMARISconfiguration.exe")
    print("Openning Simaris 2.3 FY19-20...")

def Simaris_3_0_19_20():
    os.startfile("C:/Program Files/SIEMENS/SIMARIS configuration/3.0 FY19-20/SIMARISconfiguration.exe")
    print("Openning Simaris 3.0 FY19-20...")

def Monitor():
    os.startfile("C:/UserData/z003vuba/Product Cost (Gabriel Antonio Do Prado Santos)/40 Material Cost Monitor/Dashboards/Protótipo_3/Material Cost Monitor.pbix")
    messagebox.showinfo("Say Hello", "Hello World")
    print("Material-Cost-Monitor is running...")


root = Tk()
root.title("SI-DS Product Cost Menu")
root.geometry("600x400")
menu = Menu(root)
root.iconbitmap(r'C:/UserData/z003vuba/Documents/07 Projetos Python/material-cost-monitor/icon.ico')
root.config(menu=menu)


lv = Menu(menu, tearoff=0)
menu.add_cascade(label="LV", menu=lv)
lv.add_command(label="Database [FY20]", command=DataBaseCur)
lv.add_command(label="Summarize Calculation", command=SummarizeCalc)
lv.add_command(label="SCF 2.3 FY18-19", command=Simaris_2_3_18_19)
lv.add_command(label="SCF 2.3 FY19-20", command=Simaris_2_3_19_20)
lv.add_command(label="SCF 3.0 FY19-20", command=Simaris_3_0_19_20)


monitor = Menu(menu, tearoff=0)
menu.add_cascade(label="Monitor", menu=monitor)
monitor.add_command(label="Dashboard", command=Monitor)


mainloop()
