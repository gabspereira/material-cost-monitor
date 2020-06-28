import simaris as scf

discount = scf.Table('discount').current()
discount.head()

scf.Table('local_devices').current().head()
