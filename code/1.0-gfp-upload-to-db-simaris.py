import custom_funcs as cf
import pandas as pd
from sqlalchemy import create_engine

# list all files to upload
from os import walk
path = cf.LookUp('simaris').processed()
file_name_list = []
for (dirpath, dirnames, filenames) in walk(path):
    file_name_list.extend(filenames)
    break
print(file_name_list)

# insert a table on Simaris DB
db_dir_simaris = cf.LookUp('simaris').db_path()
conn_simaris = create_engine('sqlite:///' + db_dir_simaris)

for file_name in file_name_list:
    file_path = path + file_name
    df = pd.read_csv(file_path, encoding='utf-8', sep=',')
    df.to_sql(file_name[:-4], con=conn_simaris, if_exists="replace", index=False)
    #conn_simaris.execute("SELECT * FROM '01_discount'").fetchall()
    print(file_name[:-4] + ' uploaded to db complete! [OK]')
