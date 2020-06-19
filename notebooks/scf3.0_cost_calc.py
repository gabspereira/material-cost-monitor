#main libraries
import custom_funcs as cf
import pandas as pd
import os

fi = 1.26
usd = 3.8190
eur = 4.43
corr = eur / usd


# articlenumber to find out
lookup_list = pd.read_excel('articlenumbers.xlsx', header=None)
lookup_list = lookup_list.rename(columns={0: 'articlenumber'})

# database sources connetion
csv_dir = cf.LookUp('simaris').processed()
discount = pd.read_csv(csv_dir + '01_discount.csv', encoding='utf-8')
devices1 = pd.read_csv(csv_dir + '02_siemens_devices.csv', encoding='utf-8')
devices2 = pd.read_csv(csv_dir + '03_siemens_devices2.csv', encoding='utf-8')
local_devices = pd.read_csv(csv_dir + '04_local_devices.csv', encoding='utf-8')
components = pd.read_csv(csv_dir + '05_components.csv', encoding='utf-8')
single_parts = pd.read_csv(csv_dir + '06_single_parts.csv', encoding='utf-8')


# Simaris material cost calculation
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
