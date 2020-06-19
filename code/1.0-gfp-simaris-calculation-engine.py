#main libraries
import custom_funcs as cf
#import simaris_calc_rules as calc
import pandas as pd
import os

# premisses according to FTA20:
usd = 3.819
eur = 4.43
reg_trans_land = 1 + 17/100 + 9/100
reg_trans_short = 1 + 17/100 + 28/100
fi = 1.26
usd = 3.8190
eur = 4.43
corr = eur / usd

# articlenumber to find out
lookup_list = pd.read_excel('C:/UserData/z003vuba/Documents/07 Projetos Python/articlenumbers.xlsx', header=None)
lookup_list = lookup_list.rename(columns={0: 'articlenumber'})

lookup_list

# database sources connetion
csv_dir = cf.LookUp('simaris').processed()
discount = pd.read_csv(csv_dir + '01_discount.csv', encoding='utf-8')
devices1 = pd.read_csv(csv_dir + '02_siemens_devices.csv', encoding='utf-8')
devices2 = pd.read_csv(csv_dir + '03_siemens_devices2.csv', encoding='utf-8')
local_devices = pd.read_csv(csv_dir + '04_local_devices.csv', encoding='utf-8')
components = pd.read_csv(csv_dir + '05_components.csv', encoding='utf-8')
single_parts = pd.read_csv(csv_dir + '06_single_parts.csv', encoding='utf-8')


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

df.to_excel('report.xlsx', index=False)
os.startfile('report.xlsx')
print('\n Process complete! [INFO]')
