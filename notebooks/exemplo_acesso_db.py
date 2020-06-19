import custom_funcs as cf
import pandas as pd
from sqlalchemy import create_engine

db_dir = cf.LookUp('simaris').db_path()
connection = create_engine('sqlite:///' + db_dir)
connection.table_names()
query = "SELECT * FROM NXAIR_W"

result = pd.read_sql(query, connection)
result.head()

search_list = result['material'].unique()
pd.DataFrame(search_list).to_excel(r'C:\Users\z003vuba\Desktop\lista.search_list.xlsx')

hv_door = "SELECT * FROM NXAIR_W WHERE lower(description) LIKE '%hv%door%'"
pd.read_sql(hv_door, connection).head()

compras_sap = "SELECT * FROM export"
pd.read_sql(compras_sap, connection).head()


ex = "SELECT * FROM '06_single_parts' WHERE articlenumber LIKE '8PQ%' AND import = 1"
pd.read_sql(ex, connection).head()
df = pd.read_sql(ex, connection)
df['currency_sign'].unique()
df[df['currency_sign'] == 'USD']
