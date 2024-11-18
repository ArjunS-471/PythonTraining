from pymongo import MongoClient
import pandas as pd
from bson.objectid import ObjectId

connection_string = r"mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(connection_string, tlsAllowInvalidCertificates = True)
    print("connected to mongo atlas success")

    #connect to mongo cluster
    db = client['ust_live_quiz']

    #access a collection
    collection = db['basic_collection_test']

    doc_id = "673838fa9e809b1717f1324b"
    query = {"_id" : ObjectId(doc_id)}

    update = {"$set" : {"name" : "arjun", "age" : "37"}}

    result = collection.update_one(query, update)

    if (result.matched_count > 0):
        print("there was a match, document has been found")

except Exception as e:
    print(e)

finally:
    client.close()
