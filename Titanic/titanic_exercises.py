import pandas as pd

df = pd.read_csv(r"C:\Users\Administrator\Desktop\UST_TRAINING\Titanic\titanic.csv")

#1. compare the average age of passengers who survived with those who did not

# avg_age_survived = df[df['Survived']==1]['Age'].mean()
# avg_age_notsurvived = df[df['Survived']==0]['Age'].mean()
# print(avg_age_survived,avg_age_notsurvived)

#2. Calculate the Survival rate by gender
#survival_rate = df.groupby(['Sex'])['Survived'].mean() * 100
#print(survival_rate)

#3. Create family size
df['FamilySize'] = df['SibSp'] + df['Parch']
#print(df)

#4.1 calculate average survival rate by family size
#avg_survival_familysize = df[df['Survived']==1]['FamilySize'].mean()
#print(avg_survival_familysize)

family_survival = df.groupby('FamilySize')['Survived'].mean().reset_index()
family_survival.columns = ['FamilySize','FamilySizeRate']
print(family_survival)

#4.2 Merge family survival rate back into the original dataframe
#df['AvgSurvivalRate'] = df[df['Survived']==1]['FamilySize']
df = pd.merge(df,family_survival,on='FamilySize',how='left')

#4.3 Display the merged dataframe
print(df[['FamilySize','FamilySizeRate']].head(10))
