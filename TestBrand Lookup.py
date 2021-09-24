import pandas as pd

df_brands = pd.read_csv('Files//Brands 2021-09-24.csv')
#df_helmets = pd.read_csv('Files//SBS Helmets 2021-09-24.csv')

print(df_brands.head())
list_of_brands = df_brands['Brand'].tolist()


print(list_of_brands)

