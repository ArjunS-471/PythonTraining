import pandas as pd

data1={
    'Name' : ['RRR', 'ABC', 'XYZ','Rajiv'],
    'Age' : [99,22,18,10],
    'Birth City' : ['Bangalore', 'Chennai', 'Hyderabad','Mumbai']
}

data2 = {
    'Name' : ['RRR', 'ABC', 'XYZ'],
    'Work Experience' : [1,2,3],
    'Work City' : ['NYC', 'BRK', 'LA']
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

#print(pd.merge(df1,df2,on='Name'))

#print(pd.merge(df1,df2,on='Name',how='left'))
#print(pd.merge(df1,df2,on='Name',how='outer'))


df3 = pd.merge(df1,df2,on='Name',how='outer')
avg = df3['Work Experience'].mean()
print(avg)

#df3.loc[df3['Name'] == 'Rajiv', 'Work Experience'] = df3['Work Experience'].mean()

df3['Work Experience'].fillna(avg,inplace= True)
df3['Work City'].fillna('Chennai',inplace=True)

def lowerFunction(df3):
    return df3.lower()

df3['Work City'] = df3['Work City'].apply(lowerFunction)

#New column
#df3['New column'] = 'Is Even'
#Work experience is even number or not
def evenOdd (val):
    return val % 2 == 0
df3['Is Even'] = df3['Work Experience'].apply(evenOdd)

print(df3)

# Save to CSV file
#df3.to_csv('test_output.csv', index=False)


