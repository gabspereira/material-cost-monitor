import custom_funcs as cf
import pandas as pd

#check data (PMD vs. SCF) for materials below.
#3WL1116-2CB68-4GA4-ZK07+R16+R21+R30
#3WL1225-2EB78-4GA4-ZK07+R16+R21+R30
#3WL1340-4EB68-4GA4-ZK07+R16+R21+R30


#Note: consedering ICBs from LP the landed factor should be include.

dir = cf.LookUp('simaris').processed()

devices = pd.read_csv(dir + '02_siemens_devices.csv', encoding='utf-8')
#devices[devices['articlenumber'].str.contains('3WL1116-2')].to_excel('simulatio.xlsx')


discount = pd.read_csv(dir + '01_discount.csv', encoding='utf-8')
discount[discount['discount_origin'].str.contains('3_W_L')]
