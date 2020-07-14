import pandas as pd

discount = pd.read_csv('C:/UserData/z003vuba/Product Cost (Gabriel Antonio Do Prado Santos)/40 Material Cost Monitor/data/processed/simaris/01_discount.csv', encoding='utf-8')
devices = pd.read_csv('C:/UserData/z003vuba/Product Cost (Gabriel Antonio Do Prado Santos)/40 Material Cost Monitor/data/processed/simaris/02_siemens_devices.csv', encoding='utf-8')
reg = pd.read_csv('C:/UserData/z003vuba/Product Cost (Gabriel Antonio Do Prado Santos)/40 Material Cost Monitor/data/processed/simaris/08_regulative.csv', encoding='utf-8')



devices[(devices['articlenumber'].str.contains('3WL1340-4') == True) & (devices['articlenumber'].str.contains('68-') == True)]


discount[discount['discount_origin'].str.contains('3_W_L') == True]



discount[discount['discount_origin'] == '3745']



mat_cst = 34452.0
disc = 91.87
eur = 4.80
usd = 4.25

eur_fta = 4.43
usd_fta = 3.819
conv = eur_fta/usd_fta


4.43/3.819


L_price = 37712.00
L_price/mat_cst


mat = mat_cst * 1.26 * (1 - .9187) * usd / conv
mat

16418.35/mat


mat_cst * (1 - .9187) * 1.26 * usd / (eur_fta/usd_fta)


# 3WL1340-4EG68-5FA4-ZC22+F02+R16+R21+R30+S07
(((34452.0 * (1 - .9187)) * 1.26) * 4.25) / 1.16



# 6SL3244-0BB13-1FA0
devices[(devices['articlenumber'].str.contains('6SL3244-0BB13-1FA0') == True)]

(((517.5688 * (1 - 71/100)) * 1.26) * 4.25) / 1.16



#@Flavio
3065.99 * usd * 1.26
