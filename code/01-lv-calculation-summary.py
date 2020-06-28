import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

#Ask to open the exported calculation report from Simaris
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

#transform in a DataFrame
df = pd.read_excel(filename, header=23)
df = df.iloc[:, 0:15]


df.dropna(subset=['Costs w CR Adj [BRL]'], inplace=True)

#Summarize the report
portion = df.groupby('Article number')['Quantity'].sum()
portion = portion.reset_index()


portion['Quantity'] = pd.to_numeric(portion['Quantity'], errors='coerce')
portion.dropna(subset=['Quantity'], inplace=True)
portion['Quantity'] = portion['Quantity'].astype(int)
portion = portion.sort_values(by=['Quantity'], ascending=False)

portion = portion.merge(df[['Article number', 'Costs w CR Adj [BRL]']], on='Article number', how='left')

#Export the DataFrame as a report
portion.to_excel('C:/Temp/report.xlsx', index=False)
os.startfile('C:/Temp/report.xlsx')
