from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = r"mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), tlsAllowInvalidCertificates = True)

#Send a ping to confirm the succesful connection

try:
    client.admin.command('ping')
    print('pinged your deployment, you are successfully connected')
except Exception as e:
    print(e)