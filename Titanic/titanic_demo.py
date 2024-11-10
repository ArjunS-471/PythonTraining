import pandas as pd

df = pd.read_csv(r"C:\Users\Administrator\Desktop\UST_TRAINING\Titanic\titanic.csv")
#print(df.head())

#print first 5 rows of age column
#print(df['Age'].head())
#print(df.loc[0:4,'Age'])
#print(df.loc[:,'Age'].head(5))

#Create a subset of a dataframe with only 2 columns - Age and Sex
#print(df[['Age','Sex']].head())     #column names inside a list

#filterout all the people whose age is < 25 and print
#print(df[df['Age']<25])

#Number of rows
#print(len(df.index))

#Average
#print(df['Age'].mean())
#print(df['Age'].sum()/len(df.index))

#Average of multiple function
df_male = df[df['Sex'] == 'male']
#print(df_male)
df_age = df_male[df_male['Age']<25]
#print(df_age['Fare'].mean())

df_final = df[(df['Sex'] == 'male') & (df['Age'] < 25)]
#print(df_final['Fare'].mean)

#What percentage of passengers survived the titanic
survived_pass = len(df[df['Survived'] == 1].index)
total_pass = len(df.index)
print((survived_pass/total_pass)*100)

