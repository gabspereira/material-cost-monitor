from IPython.display import display
pd.options.display.max_columns = None
import pandas as pd


df = pd.read_excel("S:/EM_MS/EM_MS_BA/Controladoria/CO_OP/Cost Controlling/Product Cost/1 NxTools_Cost+/Browser Devices/Atualização LV Browser Junho 2020/Análise.xlsx")
dg = pd.read_excel("S:/EM_MS/EM_MS_BA/Controladoria/CO_OP/Cost Controlling/Product Cost/1 NxTools_Cost+/Browser Devices/Atualização LV Browser Junho 2020/DDL DG FY_20.xlsx", sheet_name="Análise DG",header=2)


df = df[['Device', 'Import', 'Purchase price (EP)', 'in', 'PUR PRICE', 'Currency']].round(2)
#devices which are in EUR or USD and flagged Import = no and has purchase order
#df = new[(new['in'] != 'BRL') & (new['PUR PRICE'].notna() == True)].round(2)

df.loc[df['in'] == df['Currency'], 'new_cost'] = df['PUR PRICE'] #Se Currency iguas, então utiliza a ultima compra
df.loc[df['in'] == df['Currency'], 'new_currency'] = df['Currency'] #Se Currency iguas, então mantem-se a moeda

df.loc[df['in'] != df['Currency'], 'new_cost'] = df['Purchase price (EP)']/1.23 #Se Currency diferente, então utiliza a ultima compra
df.loc[df['in'] != df['Currency'], 'new_currency'] = df['in'] #Se Currency diferente, então utiliza a ultima compra


df.loc[(df['in'] == 'USD') & (df['Currency'] == 'EUR'), 'new_cost'] = df['PUR PRICE']
df.loc[(df['in'] == 'USD') & (df['Currency'] == 'EUR'), 'new_currency'] = df['Currency']


dg = dg[dg['Material'].str.contains('A7B')]

dg['material_cost_in_EUR'] = (dg['Valor Fatura'] / dg['Câmbio Proposta']) / dg['Quantidade']

df = df.merge(dg[['Material', 'material_cost_in_EUR']], how='left', left_on='Device', right_on='Material')


df.loc[df['material_cost_in_EUR'].notna() == True, 'new_cost'] = df['material_cost_in_EUR'] / 1.23
df.loc[df['material_cost_in_EUR'].notna() == True, 'new_currency'] = 'EUR'

df.to_excel('S:/EM_MS/EM_MS_BA/Controladoria/CO_OP/Cost Controlling/Product Cost/1 NxTools_Cost+/Browser Devices/Atualização LV Browser Junho 2020/2020-07-02-new-device-cost.xlsx', index=False)
