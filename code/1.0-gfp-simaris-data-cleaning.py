import custom_funcs as cf
import pandas as pd

path = cf.LookUp('simaris').raw()
path_processed = cf.LookUp('simaris').processed()


# list all files into the folder
from os import walk

raw_files = []
for (dirpath, dirnames, filenames) in walk(path):
    raw_files.extend(filenames)
    break
raw_files = raw_files[:-1] # remove 01_discounts.xlsx from the list
print(raw_files)
for file_to_clean in raw_files:
    df = pd.read_excel(path + file_to_clean)
    df.dropna(axis=1, how='all', inplace=True)
    df.to_csv(path_processed + file_to_clean[:-4] + 'csv', index=False, encoding='utf-8')
    print(file_to_clean + ' was processed and converted to csv format. [OK]')
    break
