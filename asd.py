# importing the module
import pandas as pd

# creating the DataFrame
df = pd.DataFrame({'Munkavállaló törzsszáma': {0: 23, 1: 43, 2: 12,
                                  3: 13, 4: 67, 5: 89,
                                  6: 90, 7: 56, 8: 34},
                           'Munkavállaló neve': {0: 'Ram', 1: 'Deep',
                                    2: 'Yash', 3: 'Aman',
                                    4: 'Arjun', 5: 'Aditya',
                                    6: 'Divya', 7: 'Chalsea',
                                    8: 'Akash'},
                           'Költséghelye': {0: 89, 1: 97, 2: 45, 3: 78,
                                     4: 56, 5: 76, 6: 100, 7: 87,
                                     8: 81},
                           'Megnevezés': {0: 'B', 1: 'A', 2: 'F', 3: 'C',
                                     4: 'E', 5: 'C', 6: 'A', 7: 'B',
                                     8: 'B'},
                            'Kezdete': {0: 89, 1: 97, 2: 45, 3: 78,
                                     4: 56, 5: 76, 6: 100, 7: 87,
                                     8: 81},
                            'Vége': {0: 89, 1: 97, 2: 45, 3: 78,
                                     4: 56, 5: 76, 6: 100, 7: 87,
                                     8: 81},
                            'Napok száma': {0: 89, 1: 97, 2: 45, 3: 78,
                                     4: 56, 5: 76, 6: 100, 7: 87,
                                     8: 81}})

# getting rid of the index row
df.set_index('Munkavállaló törzsszáma', inplace=True)

# determining the name of the file
file_name = 'MarksData.xlsx'

# saving the excel
df.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')