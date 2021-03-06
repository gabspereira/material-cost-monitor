import custom_funcs as cf
import pandas as pd
from sqlalchemy import create_engine

# list all files to upload
from os import walk
path = cf.LookUp('sap').processed()
file_name_list = []
for (dirpath, dirnames, filenames) in walk(path):
    file_name_list.extend(filenames)
    break
print(file_name_list)

# insert a table on sap DB
db_dir_sap = cf.LookUp('sap').db_path()
conn_sap = create_engine('sqlite:///' + db_dir_sap)

for file_name in file_name_list:
    file_path = path + file_name
    df = pd.read_csv(file_path, encoding='utf-8', sep=',')
    df.to_sql(file_name[:-4], con=conn_sap, if_exists="replace", index=False)
    #conn_sap.execute("SELECT * FROM '01_discount'").fetchall()
    print(file_name[:-4] + ' uploaded to db complete! [OK]')
