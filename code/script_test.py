#script_test.py
import sys, os
cwd = os.getcwd() + '/06 material-cost-monitor/material-cost-monitor/src'
sys.path.insert(1, cwd)

import custom_funcs as cf

cf.SendMessage()
