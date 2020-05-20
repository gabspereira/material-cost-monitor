import custom_funcs as cf
import pandas as pd
from sqlalchemy import create_engine


# select processed file
file_name = '01_discount.csv'
file_path = cf.LookUp('simaris').processed() + file_name

df = pd.read_csv(file_path, encoding='utf-8', sep=',')

# insert a table on db
db_dir = cf.LookUp('simaris').db_path()
connection = create_engine('sqlite:///' + db_dir)
df.to_sql('01_discount', con=connection, if_exists="replace", index=False)
connection.execute("SELECT * FROM '01_discount'").fetchall()
print('Upload to db complete!')
