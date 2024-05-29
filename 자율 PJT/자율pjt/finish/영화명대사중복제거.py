import pandas as pd

df1 = pd.read_excel('./영화명대사최종.xlsx')

df1.drop_duplicates(inplace=True)

df1.to_excel('영화명대사최최종.xlsx', index=False)
