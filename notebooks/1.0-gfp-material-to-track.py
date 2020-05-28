import custom_funcs as cf
import pandas as pd
from sqlalchemy import create_engine

db_dir = cf.LookUp('nxtools').db_path()
connection = create_engine('sqlite:///' + db_dir)

query = "SELECT * FROM 'Assembly Group'"


result = pd.read_sql(query, connection)

result.head()
