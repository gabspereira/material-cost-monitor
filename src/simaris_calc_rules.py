#this file intends to calculate any material into Simaris and return an material cost

landed_factor = 1.26
usd = 3.8190
eur = 4.43
scf_usd_correction = eur / usd

class MatCost:

    # def __new__(self, cost, currency, discount):
    #     self.cost = cost
    #     self.currency = currency
    #     self.discount = discount
    #
    #     if currency == 'USD':
    #         mat_cost = cost * (1 - discount/100) * landed_factor * usd / scf_usd_correction
    #     elif currency == 'EUR':
    #         mat_cost = cost * (1 -discount/ 100) * landed_factor * eur
    #     elif currency == 'BRL':
    #         mat_cost = cost
    #     else:
    #         print('Currency not localized!')
    #
    #     return mat_cost


    def __new__(self, x):
        self.cost = x[5]
        self.currency = x[4]
        self.discount = x[9]
        return cost
