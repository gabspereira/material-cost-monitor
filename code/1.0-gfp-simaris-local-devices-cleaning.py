import custom_funcs as cf
import pandas as pd

path = cf.LookUp('simaris').raw()
path_processed = cf.LookUp('simaris').processed()



local_devices = pd.read_excel(path + '04_local_devices.xlsx')
local_devices.dropna(axis=1, inplace=True)
drop_list = ['description_de', 'description_es', 'tree section1 de', 'tree section2 de', 'tree section1 es', 'tree section2 es']
local_devices.drop(drop_list, axis=1, inplace=True)

local_devices.to_csv(path_processed + '04_local_devices.csv', index=False, encoding='utf-8')
print('04_local_devices.csv was gerenated - OK')
