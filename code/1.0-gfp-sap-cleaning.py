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


nxair_w_1 = pd.read_excel(path + raw_files[0], skiprows=1)
columns = ['level','material','rv','qty','mu','ty','description']
nxair_w_1.drop(nxair_w_1.columns[[0,2,6,10,11]], axis=1, inplace=True)
nxair_w_1.columns = columns
nxair_w_1['level'] = nxair_w_1['level'].str.replace('.','')
nxair_w_1.head()
