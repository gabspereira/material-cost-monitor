import pandas as pd

# articlenumber to find out
lookup_list = pd.read_excel('./articlenumbers.xlsx', header=None)
lookup_list = lookup_list.rename(columns={0: 'articlenumber'})



def dash(x):
    return x[0].replace('-','')

def br(x):
    if '8PQ' in x[0]:
        return x[0] + 'BR'
    else:
        return x[0]


lookup_list['articlenumber'] = lookup_list.apply(dash, axis=1)

lookup_list['articlenumber'] = lookup_list.apply(br, axis=1)

lookup_list.to_excel('./articlenumbers.xlsx', index=False, header=False)
