#main libraries
import simaris as scf
from tkinter import Tk
from tkinter.filedialog import askopenfilename
#import simaris_calc_rules as calc
import pandas as pd
import os

# premisses according to FTA20:
usd = 3.819
eur = 4.43
reg_trans_land = 1 + 17/100 + 9/100
reg_trans_short = 1 + 17/100 + 28/100
fi = 1.26
corr = eur / usd

# articlenumber to find out
print("Please select an Excel file with contains the list of articlenumbers you want to find into the LV Database [FY20].")
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

lookup_list = pd.read_excel(filename, header=None)
lookup_list = lookup_list.rename(columns={0: 'articlenumber'})

lookup_list

# database sources connetion
discount = scf.Table('discount').current()
devices1 = scf.Table('devices1').current()
devices2 = scf.Table('devices2').current()
local_devices = scf.Table('local_devices').current()
components = scf.Table('components').current()
single_parts = scf.Table('single_parts').current()


# -- Start: Simaris material cost calculation
devices1 = devices1.merge(discount, left_on='brand_group', right_on='discount_origin')


devices1.loc[devices1['currency_sign'] == 'USD', 'mat_cost_brl'] = devices1['cost'] * (1 - devices1['discount1']/100) * fi * usd / corr
devices1.loc[devices1['currency_sign'] == 'EUR', 'mat_cost_brl'] = devices1['cost'] * (1 - devices1['discount1']/100) * fi * eur
devices1.loc[devices1['currency_sign'] == 'BRL', 'mat_cost_brl'] = devices1['cost']

devices2['cost'].replace(to_replace=',', value='.', inplace=True, regex=True)
devices2['cost'] = devices2['cost'].astype('float', copy=True)
devices2.loc[devices2['currency_sign'] == 'BRL', 'mat_cost_brl'] = devices2['cost']
devices2.loc[devices2['currency_sign'] == 'EUR', 'mat_cost_brl'] = devices2['cost'] * fi * eur

local_devices.loc[(local_devices['import'] == 1) & (local_devices['currency_sign'] == 'EUR'), 'mat_cost_brl'] = local_devices['price'] * fi * eur
local_devices.loc[(local_devices['import'] == 1) & (local_devices['currency_sign'] == 'USD'), 'mat_cost_brl'] = local_devices['price'] * fi * usd / corr
local_devices.loc[(local_devices['import'] == 0) & (local_devices['currency_sign'] == 'USD'), 'mat_cost_brl'] = local_devices['price'] * usd / corr
local_devices.loc[(local_devices['import'] == 0) & (local_devices['currency_sign'] == 'EUR'), 'mat_cost_brl'] = local_devices['price'] * eur
local_devices.loc[local_devices['currency_sign'] == 'BRL', 'mat_cost_brl'] = local_devices['price']

# Labor cost not included
components.loc[(components['import'] == 1) & (components['currency_sign'] == 'EUR'), 'mat_cost_brl'] = components['cost'] * fi * eur
components.loc[components['currency_sign'] == 'EUR', 'mat_cost_brl'] = components['cost'] * eur
components.loc[components['currency_sign'] == 'BRL', 'mat_cost_brl'] = components['cost']

single_parts.loc[(single_parts['import'] == 1) & (single_parts['currency_sign'] == 'EUR'), 'mat_cost_brl'] = single_parts['cost'] * fi * eur
single_parts.loc[single_parts['currency_sign'] == 'EUR', 'mat_cost_brl'] = single_parts['cost'] * eur
single_parts.loc[single_parts['currency_sign'] == 'BRL', 'mat_cost_brl'] = single_parts['cost']

# -- End: Simaris material cost calculation


# look up inside each table and get cost details
df = pd.DataFrame()
for index, row in lookup_list.iterrows():
    articlenumber = row['articlenumber']

    df_dummy1 = devices1[devices1['articlenumber'] == articlenumber]
    df_dummy2 = devices2[devices2['articlenumber'] == articlenumber]
    df_dummy3 = local_devices[local_devices['articlenumber'] == articlenumber]
    df_dummy4 = components[components['articlenumber'] == articlenumber]
    df_dummy5 = single_parts[single_parts['articlenumber'] == articlenumber]

    try:
        if len(df_dummy1) != 0:
            print(str(articlenumber) + ' is into devices1 table.' + ' [OK]')
            df = pd.concat([df, df_dummy1], sort=False)
        elif len(df_dummy2) != 0:
            print(str(articlenumber) + ' is into devices2 table.' + ' [OK]')
            df = pd.concat([df, df_dummy2], sort=False)
        elif len(df_dummy3) != 0:
            print(str(articlenumber) + ' is into local devices table.' + ' [OK]')
            df = pd.concat([df, df_dummy3], sort=False)
        elif len(df_dummy4) != 0:
            print(str(articlenumber) + ' is into components table.' + ' [OK]')
            df = pd.concat([df, df_dummy4], sort=False)
        elif len(df_dummy5) != 0:
            print(str(articlenumber) + ' is into single_parts table.' + ' [OK]')
            df = pd.concat([df, df_dummy5], sort=False)
    except:
        print(str(articlenumber) + ' was not found in any table. [INFO]')

# get discount according to first of all article number and second from VPCK




# Consolidate data in a single report

df.to_excel('C:/Temp/report.xlsx', index=False)
os.startfile('C:/Temp/report.xlsx')
print('\n Process complete! [INFO]')
