import custom_funcs as cf
import pandas as pd
from sqlalchemy import create_engine

db_dir = cf.LookUp('simaris').db_path()
connection = create_engine('sqlite:///' + db_dir)
connection.table_names()


query = "SELECT * FROM '02_siemens_devices' WHERE articlenumber LIKE '6SL3202%'"

pd.read_sql(query, connection).head()

# ex = "SELECT * FROM '06_single_parts' WHERE articlenumber LIKE '8PQ%' AND import = 1"
# pd.read_sql(ex, connection).head()
# df = pd.read_sql(ex, connection)
# df['currency_sign'].unique()
# df[df['currency_sign'] == 'USD']
