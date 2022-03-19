import pandas as pd

df = pd.ExcelWriter('表清单.xlsx',engine='openpyxl')
for i in range(2,5):
    df.to_excel(r'表清单.xlsx',sheet_name='sheet'+str(i),index=False)