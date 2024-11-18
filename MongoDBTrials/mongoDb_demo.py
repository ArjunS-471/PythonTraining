from pymongo import MongoClient
import pandas as pd

#connection_string = r"mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
connection_string = r"mongodb+srv://arjun471:jIOhxMODLAGYAMKH@cluster0.moex3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(connection_string, tlsAllowInvalidCertificates = True)
    print("connected to mongo atlas success")

    #connect to mongo cluster
    db = client['sample_mflix']
    #db = client['ust_live_quiz']

    #access a collection
    collection = db['movies']

    # sample_data = {
    #     "fighter1" : "Tyson",
    #     "fighter2" : "Jake",
    #     "watchedMatch" : False,
    #     "result" : "Tyson lost",
    # }
    # collection.insert_one(sample_data)
    # print("insert successful")

    #query the collection
    results = collection.find()
    # for doc in results:
    #     print(doc)
    #     break

    result_list = list(results)

    df = pd.DataFrame(result_list)
    print(df.head(100))
    # print(df.columns)

except Exception as e:
    print(e)

finally:
    client.close()
