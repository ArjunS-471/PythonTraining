from pymongo import MongoClient
import pandas as pd
import numpy as np
import sqlite3
import json

def is_list_or_dict(value):
    return isinstance(value, (list, dict))

def convert_to_json(value):
    if isinstance(value, (list, dict)):
        return json.dumps(value)
    return value

def is_custom_object(value):
    return isinstance(value, object) and not isinstance (value, (str, float, int, bool))

def convert_to_str(value):
    return str(value)

connection_string = r"mongodb+srv://arjun471:jIOhxMODLAGYAMKH@cluster0.moex3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#Setting connection to a local sqllite DB
connSQL = sqlite3.connect(r'C:\Users\Administrator\Desktop\UST_TRAINING\Milestone 3\Milestone3.sqlite')

try:
    client = MongoClient(connection_string, tlsAllowInvalidCertificates = True)
    print("connected to mongo atlas success")

    #connect to mongo cluster
    db = client['sample_mflix']

    #access a collection
    collection = db['movies']

    results = collection.find()
    
    df = pd.DataFrame(results)
    
    #Temporary code to confirm the Table structure
    #df.to_csv('output.csv', index = False)

    #modifying column format
    for column in df.columns:
        try:
            if pd.api.types.is_datetime64_any_dtype(df[column]):
                df[column] = df[column].dt.strftime('%Y-%m-%d %H:%M:%S')
            
            if df[column].apply(is_list_or_dict).any():
                df[column] = df[column].apply(convert_to_json)
            
            if df[column].apply(is_custom_object).any():
                df[column] = df[column].apply(convert_to_str)

            df[column] = df[column].replace({pd.NA: None, pd.NaT: None, np.nan: None})
        except Exception as e:
            print("In loop try -", e,df[column].name)
            columnName = df[column].name

    #Deleting this column since could not add this to DB directly due to some format issue
    df.drop([columnName], axis = 'columns', inplace = True)

    df.to_sql('Milestone', connSQL)
    connSQL.commit()
    print('Succesfully commited')
    connSQL.close()

except Exception as e:
    print('Outer try',e)

finally:
    client.close()