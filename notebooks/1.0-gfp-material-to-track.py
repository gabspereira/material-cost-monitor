import custom_funcs as cf
import pandas as pd
from sqlalchemy import create_engine

db_dir = cf.LookUp('simaris').db_path()
connection = create_engine('sqlite:///' + db_dir)

query = "SELECT * FROM '02_siemens_devices'"


discount = pd.read_sql(query, connection)

discount.head(1)
