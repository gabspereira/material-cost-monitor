import sys, os
cwd = os.getcwd() + '/material-cost-monitor/src'
sys.path.insert(1, cwd)

#import main custom functions
import custom_funcs as cf

path = cf.LookUp('simaris').raw()
path_processed = cf.LookUp('simaris').processed()

# 01 - Discount list
discount = pd.read_excel(path + '01_discount.xlsx')
discount.head()
discount.tail()

# 01.1 - Discount by Article number

art_nr_bodies = discount[discount['articlenumber_body'].notnull()]
art_nr_bodies = art_nr_bodies[['articlenumber_body', 'discount1']]
art_nr_bodies = art_nr_bodies.rename(columns={"articlenumber_body": "discount_origin"})
art_nr_bodies.head()

# 01.2 - Discount by Group

group = discount[discount['discount group'].notnull()]
group = group[['discount group', 'discount1']]
group = group.rename(columns={"discount group": "discount_origin"})
group.head()


# 01.3 - Discount by VPCK ('brand_group')

vpck = discount[discount['brand_group'].notnull()]
vpck = vpck[['brand_group', 'discount1']]
vpck = vpck.rename(columns={"brand_group": "discount_origin"})
vpck.head()


# To simplify the orgin of the discounts a new column will be set to agroup all discounts in a single place

discount = pd.concat([group, vpck, art_nr_bodies])
discount.to_csv(path_processed + '01_discount.csv', index=False, encoding='utf-8')
