#script_test.py
import sys, os
cwd = os.getcwd() + '/material-cost-monitor/src'
sys.path.insert(1, cwd)

#import main custom functions
import custom_funcs as cf
import database as db
#---------------------------

# - just a test to call a module --- #
cf.SendMessage()

# - test to return an output from module --- #
dir = cf.LookUp('simaris').raw()
db_dir = cf.LookUp('nxtools').db_path()

# - test to connect with DB and execute commands --- #
conn = db.conn(db_dir)
c = conn.cursor()
c.execute("select name from sqlite_master where type = 'table'")
print(c.fetchall())
conn.commit()
conn.close()
