import custom_funcs as cf
import pandas as pd
from sqlalchemy import create_engine

# list all files to upload
from os import walk
path = cf.LookUp('nxtools').processed()
file_name_list = []
for (dirpath, dirnames, filenames) in walk(path):
    file_name_list.extend(filenames)
    break
print(file_name_list)

# insert a table on nxtools DB
db_dir_nxtools = cf.LookUp('nxtools').db_path()
conn_nxtools = create_engine('sqlite:///' + db_dir_nxtools)

for file_name in file_name_list:
    file_path = path + file_name
    df = pd.read_csv(file_path, encoding='utf-8', sep=',')
    df.to_sql(file_name[:-4], con=conn_nxtools, if_exists="replace", index=False)
    #conn_nxtools.execute("SELECT * FROM '01_discount'").fetchall()
    print(file_name[:-4] + ' uploaded to db complete! [OK]')
