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
        else:
            print('Available options: nxtools, simaris, salesforce')
            dir = 'Test: Error to get directory.'
        return dir

    def processed(self):
        if self.tool == 'nxtools':
            dir = self.data_path + '/processed/nxtools/FY20/'
        elif self.tool == 'simaris':
            dir = self.data_path + '/processed/simaris/SCF2.4/'
        elif self.tool == 'salesforce':
            dir = self.data_path + '/processed/salesforce/2020_05_05/'
        else:
            print('Available options: nxtools, simaris, salesforce')
            dir = 'Test: Error to get directory.'
        return dir


    def db_path(self):
        if self.tool == 'nxtools':
            dir = self.data_path + '/db/nxtools.db'
        elif self.tool == 'simaris':
            dir = self.data_path + '/db/simaris.db'
        elif self.tool == 'salesforce':
            dir = self.data_path + '/db/salesforce.db'
        else:
            print('Available options: nxtools, simaris, salesforce')
            dir = 'Test: Error to get directory.'
        return dir
