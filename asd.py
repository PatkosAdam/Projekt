# importing the module
import pandas as pd

# importing summary xlsx file
df2 = pd.read_excel('sum.xlsx')

# append new row
df2.loc[len(df2.index)] = [900, 'TAA', 900, 'RAAAA', 900, 900, 900] # new values
df2.set_index('Munkavállaló törzsszáma', inplace=True) # reassigning index row
df2.to_excel('sum.xlsx') # saving
print('DataFrame is written to Excel File successfully.') # successful message