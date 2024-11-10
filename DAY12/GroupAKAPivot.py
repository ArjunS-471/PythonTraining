import pandas as pd

data = {
    'Store' : ['Store1', 'Store1','Store2','Store2','Store3','Store3'],
    'Region' : ['North', 'North','South','South','East','East'],
    'Sales' : [200, 150,300,250,400,350]
}

df = pd.DataFrame(data)

print(df)

#print(df.groupby(['Store'])['Sales'].sum())
#print(df.groupby(['Region'])['Sales'].sum())

regional_sales_df = df.groupby(['Region'])['Sales'].sum()

merged_df = pd.merge(df, regional_sales_df, on = 'Region', how = 'left', suffixes = ("_Store", "_Region"))

merged_df['SalesByRegionby%'] = merged_df['Sales_Store']/merged_df['Sales_Region'] * 100

print(merged_df)