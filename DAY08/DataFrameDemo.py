import pandas as pd

data = {
    'Name' : ['A', 'B', 'C'],
    'Age' : [11,12,13],
    'Place' : ['BLR' , 'CHE', 'HYD']
}

df = pd.DataFrame(data)

print(df)