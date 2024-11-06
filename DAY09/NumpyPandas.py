import pandas as pd
import numpy as np

arr = np.array([10,15,18,22,25])
s = pd.Series(arr,index=['a','b','c','d','e'])
print(s)

s = pd.Series(50,index=[0,1,2,3,4])
print(s)