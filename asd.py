# imports
import pandas as pd
from datetime import date
import xlsxwriter

# importing summary xlsx file
df = pd.read_excel('sum.xlsx')

# variables
mv_torzsszam = 90
mv_nev = 'Bela'
koltseghely = 10
megnevezes = 're'
kezdet = date(1960, 5, 17)
veg = date(2000, 5, 20)
napok = 9

# append new row
df.loc[len(df.index)] = [mv_torzsszam, mv_nev, koltseghely, megnevezes, kezdet, veg, napok] # new values
df.set_index('Munkavállaló törzsszáma', inplace=True) # reassigning index row

# formatting
df["Vége"] = pd.to_datetime(df["Vége"]).dt.strftime("%Y-%m-%d")
df["Kezdete"] = pd.to_datetime(df["Kezdete"]).dt.strftime("%Y-%m-%d")

# saving
df.to_excel('sum.xlsx') # saving
print('DataFrame is written to Excel File successfully.') # successful message