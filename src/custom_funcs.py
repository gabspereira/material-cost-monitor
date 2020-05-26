def SendMessage():
    msg = 'Test of called function, ok...!'
    return msg

class LookUp():

    def __init__(self, tool):
        self.tool = tool
        self.data_path = 'K:/EM_MS/EM_MS_BA/Controladoria/CO_OP/Cost Controlling/Product Cost/40 Material Cost Monitor/data'

    def raw(self):
        if self.tool == 'nxtools':
            dir = self.data_path + '/raw/nxtools/FY20/'
        elif self.tool == 'simaris':
            dir = self.data_path + '/raw/simaris/SCF2.4/'
        elif self.tool == 'salesforce':
            dir = self.data_path + '/raw/salesforce/2020_05_05/'
        elif self.tool == 'compras':
            dir = self.data_path + '/raw/compras/FY20/'
        else:
            print('Available options: nxtools, simaris, salesforce, compras')
            dir = 'Test: Error to get directory.'
        return dir

    def processed(self):
        if self.tool == 'nxtools':
            dir = self.data_path + '/processed/nxtools/'
        elif self.tool == 'simaris':
            dir = self.data_path + '/processed/simaris/'
        elif self.tool == 'salesforce':
            dir = self.data_path + '/processed/salesforce/'
        elif self.tool == 'compras':
            dir = self.data_path + '/processed/compras/'
        else:
            print('Available options: nxtools, simaris, salesforce, compras')
            dir = 'Test: Error to get directory.'
        return dir


    def db_path(self):
        if self.tool == 'nxtools':
            dir = self.data_path + '/db/nxtools.db'
        elif self.tool == 'simaris':
            dir = self.data_path + '/db/simaris.db'
        elif self.tool == 'salesforce':
            dir = self.data_path + '/db/salesforce.db'
        elif self.tool == 'compras':
            dir = self.data_path + '/db/compras.db'
        else:
            print('Available options: nxtools, simaris, salesforce, compras')
            dir = 'Test: Error to get directory.'
        return dir
