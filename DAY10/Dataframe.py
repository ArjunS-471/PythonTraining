import pandas as pd

#name = pd.Series(['Rohit','Kohli'])
#team = pd.Series(['MI','RCB'])

dic = {
    'Name' : ['Rohit', 'Virat'],
    'Team' : ['MI', 'RCB']
}

#dic = {'Name' : name, 'Team' : team}

df = pd.DataFrame(dic)
print(df)

df2 = pd.DataFrame(dic, index = ['Rank 1', 'Rank 2'])

for row_index, row_value in df2.iterrows():
    print('---------------------')
    print('row index is : ', row_index)
    print('row value is : ', row_value)
    
for col_name, col_value in df2.iteritems():
    print('\n')
    print('Column name is : ', col_name)
    print('Column value is : ', col_value)