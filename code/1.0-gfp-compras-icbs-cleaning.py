import custom_funcs as cf
import pandas as pd

path = cf.LookUp('compras').raw()
path_processed = cf.LookUp('compras').processed()


# list all files into the folder
from os import walk

raw_files = []
for (dirpath, dirnames, filenames) in walk(path):
    raw_files.extend(filenames)
    break
raw_files = raw_files[:-1] # remove 01_discounts.xlsx from the list
print(raw_files)


mc = pd.read_excel(path + 'Lista preços MC FY20.xlsx', sheet_name='Lista de preços ICB - DS', skiprows=1, header=0)
mc.dropna(axis=1, how='all', inplace=True)
mc.dropna(subset=['Desconto ICB FY20 \n(Q1 e Q2)'], inplace=True)



cp = pd.read_excel(path + 'Lista preços CP FY20.xlsx', sheet_name='CP BR FY20', header=4)
cp.dropna(axis=1, how='all', inplace=True)
cp.dropna(subset=['Desconto CP BR'], inplace=True)



rabatt = pd.read_excel(path + 'Lista preços CP FY20.xlsx', sheet_name='Nova base - Jundai Rabatt FY20.', header=4)
rabatt.dropna(axis=1, how='all', inplace=True)
rabatt.dropna(subset=['EM MS customer discount BR (USD) '], inplace=True)


dffa = pd.read_excel(path + 'Lista preços DF FA FY20.xlsx', sheet_name='DF FA DE FY20', header=4)
dffa.dropna(axis=1, how='all', inplace=True)


lp = pd.read_excel(path + 'Lista preços LP FY20.xlsx', sheet_name='LP DE FY20', header=4)
lp.dropna(axis=1, how='all', inplace=True)

# for file_to_clean in raw_files:
#     df = pd.read_excel(path + file_to_clean)
#     df.dropna(axis=1, how='all', inplace=True)
#     df.to_csv(path_processed + file_to_clean[:-4] + 'csv', index=False, encoding='utf-8')
#     print(file_to_clean + ' was processed and converted to csv format. [OK]')
