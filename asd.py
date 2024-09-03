# imports
import pandas as pd
from datetime import date

# importing summary xlsx file
df2 = pd.read_excel('sum.xlsx')

# variables
mv_torzsszam = 123
mv_nev = 'nev'
koltseghely = 123
megnevezes = '???????'
kezdet = date(2020, 5, 17)
veg = date(2020, 5, 20)
napok = 123


# append new row
df2.loc[len(df2.index)] = [mv_torzsszam, mv_nev, koltseghely, megnevezes, kezdet, veg, napok] # new values
df2.set_index('Munkavállaló törzsszáma', inplace=True) # reassigning index row
df2.to_excel('sum.xlsx') # saving
print('DataFrame is written to Excel File successfully.') # successful message