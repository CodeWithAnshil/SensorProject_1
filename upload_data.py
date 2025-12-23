from pymongo.mongo_client import MongoClient
import json
import pandas as pd

# URL
url = "mongodb+srv://anshilmaurya888_db_user:1234Ansh@cluster0.nrurchl.mongodb.net/"
# Create a client and connect to server
client = MongoClient(url)

# create a databse and collection 
DATABASE_NAME = "sensors"
COLLECTION_NAME = "waferfault"

# read csv file
df = pd.read_csv("D:\SensorProject\notebooks\wafer_23012020_041211.csv")

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)