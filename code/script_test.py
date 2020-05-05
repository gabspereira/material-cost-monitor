#script_test.py
import sys, os
cwd = os.getcwd() + '/material-cost-monitor/src'
sys.path.insert(1, cwd)

import custom_funcs as cf

cf.SendMessage()


cf.LookUp('simaris').raw()
