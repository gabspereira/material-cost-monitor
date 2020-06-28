import custom_funcs as cf
import pandas as pd

# database sources connetion with Simaris 2020
csv_dir = cf.LookUp('simaris').processed()

class Table():
    def __init__(self, input):
        self.input = input

    def current(self):
        if self.input == 'discount':
            discount = pd.read_csv(csv_dir + '01_discount.csv', encoding='utf-8')
            print('Table 01_discount from 2020 was loaded. [OK]')
            return discount

        if self.input == 'devices1':
            devices1 = pd.read_csv(csv_dir + '02_siemens_devices.csv', encoding='utf-8')
            print('Table 02_siemens_devices from 2020 was loaded. [OK]')
            return devices1

        if self.input == 'devices2':
            devices2 = pd.read_csv(csv_dir + '03_siemens_devices2.csv', encoding='utf-8')
            print('Table 03_siemens_devices2 from 2020 was loaded. [OK]')
            return devices2

        if self.input == 'local_devices':
            local_devices = pd.read_csv(csv_dir + '04_local_devices.csv', encoding='utf-8')
            print('Table 04_local_devices from 2020 was loaded. [OK]')
            return local_devices

        if self.input == 'components':
            components = pd.read_csv(csv_dir + '05_components.csv', encoding='utf-8')
            print('Table 05_components from 2020 was loaded. [OK]')
            return components

        if self.input == 'single_parts':
            single_parts = pd.read_csv(csv_dir + '06_single_parts.csv', encoding='utf-8')
            print('Table 06_somgle_parts from 2020 was loaded. [OK]')
            return single_parts

        else:
            print('No DataFrame has been load. [ERROR]')
            print('Please use avaliable entries: \n discount \n devices1 \n devices2 \n local_devices \n components \n single_parts')
