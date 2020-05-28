import custom_funcs as cf
import pandas as pd
from sqlalchemy import create_engine

db_dir = cf.LookUp('sap').db_path()
connection = create_engine('sqlite:///' + db_dir)
connection.table_names()
query = "SELECT * FROM NXAIR_W"

result = pd.read_sql(query, connection)
result.head()



hv_door = "SELECT * FROM NXAIR_W WHERE lower(description) LIKE '%hv%door%'"
pd.read_sql(hv_door, connection).head()
