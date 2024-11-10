import pandas as pd
import numpy as np

data1={
    'Name' : ['RRR', 'ABC', 'Mr. XYZ'],
    'Age' : [99,22,18],
    'City' : ['Bangalore', 'Chennai', 'Hyderabad']
}

data2 = {
    'Name' : ['P','Q','R'],
    'Age' : [1,2,3],
    'City' : ['NYC', 'BRK', 'LA']
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

#df3 = pd.concat([df1,df2])
df3 = pd.concat([df1,df2], ignore_index=True)

#df3.loc[2,'City'] = 'Mumbai'

#Gives boolan for the matching row
print(df3['Name'] == 'Mr. XYZ')

#the boolean from above becomes the loc parameter
df3.loc[df3['Name'] == 'Mr. XYZ', 'City'] = 'Mumbai'
#print(df3)

df3.loc[df3['Name'] == 'Mr. XYZ', 'City'] = np.nan
df3.loc[df3['Name'] == 'RRR', 'City'] = np.nan

print(df3['City'].value_counts())

df3['City'].fillna('Chennai', inplace=True)

print(df3['City'].value_counts())




