import custom_funcs as cf
import pandas as pd

path = cf.LookUp('nxtools').raw()
path_processed = cf.LookUp('nxtools').processed()

file_to_clean = ['Assembly Group', 'Final Assembly & Testing', 'Accessories', 'Devices','Sparepart']


assy_group = pd.read_excel(path + 'NXAIR_W_Snapshot.xlsx', sheet_name='Assembly Group', header=5)
assy_group.to_csv(path_processed + file_to_clean[0] + '.csv', index=False, encoding='utf-8')
