import custom_funcs as cf
import pandas as pd
import database as db


# select processed file
file_name = '01_discount.csv'
file_path = cf.LookUp('simaris').processed() + file_name

df = pd.read_csv(file_path, encoding='utf-8', sep=',')

# connect to db
db_dir = cf.LookUp('simaris').db_path()
conn = db.conn(db_dir)
c = conn.cursor()
c.execute("select name from sqlite_master where type = 'table'")


# insert a table on db




print(c.fetchall())
conn.commit()
conn.close()
