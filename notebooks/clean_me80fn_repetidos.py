import pandas as pd

df = pd.read_excel('C:/UserData/z003vuba/Product Cost (Gabriel Antonio Do Prado Santos)/40 Material Cost Monitor/Dashboards/Protótipo_3/Bases/me80fn_Simaris.xlsx', header=0)
df.drop_duplicates(subset=['Date','Material'], keep='first').to_excel('C:\Temp\sem_duplicados.xlsx')
