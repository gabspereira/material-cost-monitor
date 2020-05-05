def SendMessage():
    msg = 'Test of called function, ok...!'
    return msg


class LookUp():
    def __init__(self, tool):
        self.tool = tool

    def raw(self):
        if self.tool == 'nxtools':
            dir_raw = 'K:/EM_MS/EM_MS_BA/Controladoria/CO_OP/Cost Controlling/Product Cost/40 Material Cost Monitor/data/raw/nxtools/FY20/'
        elif self.tool == 'simaris':
            dir_raw = 'K:/EM_MS/EM_MS_BA/Controladoria/CO_OP/Cost Controlling/Product Cost/40 Material Cost Monitor/data/raw/simaris/SCF2.4/'
        elif self.tool == 'salesforce':
            dir_raw = 'K:/EM_MS/EM_MS_BA/Controladoria/CO_OP/Cost Controlling/Product Cost/40 Material Cost Monitor/data/raw/salesforce/2020_05_05/'
        else:
            print('Available options: nxtools, simaris, salesforce')
            dir_raw = 'Test: Error to get dir_raw.'
        return dir_raw
