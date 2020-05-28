import custom_funcs as cf
import pandas as pd

path = cf.LookUp('sap').raw()
path_processed = cf.LookUp('sap').processed()


# list all files into the folder
from os import walk

raw_files = []
for (dirpath, dirnames, filenames) in walk(path):
    raw_files.extend(filenames)
    break
print(raw_files)


nxair_w_1 = pd.read_excel(path + raw_files[2], header=0)

nxair_w_1.drop(nxair_w_1.columns[[2,8,10,12,13]], axis=1, inplace=True)
columns = ['include','level','material','pur_ty','cost_block','rev','qty','mu','description']
nxair_w_1.columns = columns
nxair_w_1['level'] = nxair_w_1['level'].str.replace('.','')
#nxair_w_1.drop(nxair_w_1.index[0], inplace=True)


nxair_w_1.to_csv(path_processed + raw_files[2][:-5] + '.csv', index=False, encoding='utf-8')
