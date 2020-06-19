#main libraries
import custom_funcs as cf
import pandas as pd

#report = pd.read_excel('report.xlsx')


dir = "C:/UserData/z003vuba/Documents/07 Projetos Python/material-cost-monitor/data/"


cp = pd.read_excel(dir + 'Lista preços CP FY20.xlsx', header=4)
lp = pd.read_excel(dir + 'Lista preços LP FY20.xlsx', header=4)
dffa = pd.read_excel(dir + 'Lista preços DF FA FY20.xlsx', header=4)
mc = pd.read_excel(dir + 'Lista preços MC FY20.xlsx', header=1)

cp['family'] = cp['Erzeugnisnummer'].str[:3]
cp['family'].unique()


lp['family'] = lp['Erzeugnisnummer'].str[:3]
lp['family'].unique()

dffa['family'] = dffa['Erzeugnisnummer'].str[:3]
dffa['family'].unique()

mc.dropna(subset=['GM2'], inplace=True)
mc['family'] = mc['MLFB'].str[:3]
mc['family'].unique()
