#main libraries
import custom_funcs as cf
import pandas as pd
import numpy as np

#report = pd.read_excel('report.xlsx')


dir = "C:/UserData/z003vuba/Documents/07 Projetos Python/material-cost-monitor/data/"


cp = pd.read_excel(dir + 'Lista preços CP FY20.xlsx', header=4)
lp = pd.read_excel(dir + 'Lista preços LP FY20.xlsx', header=4)
dffa = pd.read_excel(dir + 'Lista preços DF FA FY20.xlsx', header=4)
mc = pd.read_excel(dir + 'Lista preços MC FY20.xlsx', header=1)

cp['family'] = cp['Erzeugnisnummer'].str[:3]
lista_cp = cp['family'].unique()
familia_cp = pd.DataFrame()
familia_cp['mlfb'] = lista_cp.tolist()
familia_cp['origem'] = 'CP'


lp['family'] = lp['Erzeugnisnummer'].str[:3]
lista_lp = lp['family'].unique()
familia_lp = pd.DataFrame()
familia_lp['mlfb'] = lista_lp.tolist()
familia_lp['origem'] = 'LP'


dffa['family'] = dffa['Erzeugnisnummer'].str[:3]
lista_dffa = dffa['family'].unique()
familia_dffa = pd.DataFrame()
familia_dffa['mlfb'] = lista_dffa.tolist()
familia_dffa['origem'] = 'DFFA'


mc.dropna(subset=['GM2'], inplace=True)
mc['family'] = mc['MLFB'].str[:3]
lista_mc = mc['family'].unique()
familia_mc = pd.DataFrame()
familia_mc['mlfb'] = lista_mc.tolist()
familia_mc['origem'] = 'MC'


familias = pd.concat([familia_cp, familia_lp, familia_dffa, familia_mc])
familias.to_excel('familias-icbs.xlsx', index=False)
