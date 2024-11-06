import pandas as pd

d = {'a':1,'b':2,'c':3}
ser = pd.Series(data = d, index = ['a','b','c'])
print(ser)

#Attrribute 1
print('1. At = access single value for a row/column pair by label')
print(ser.at['b'])

#Attrribute 2
print('2. Index = The index labels of the series')
print(ser.index)

#Attrribute 3
print('3. Empty = returns bool, checks if series/dataframe is empty')
print(ser.empty)

#Attrribute 4
print('4. iat = get or set a single value in a series/dataframe')
print(ser.iat[0])

#Attrribute 5
print('5. shape = returns a tuple of the shape of the underlying data')
print(ser.shape)

#Method 1
print('1. abs = return a series/dataframe with absolute numeric value of each element')
print(ser.abs())

#Method 2

#Method 3

#Method 4

#Method 5