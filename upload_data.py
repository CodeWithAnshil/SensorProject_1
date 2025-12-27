from pymongo.mongo_client import MongoClient
import json
import pandas as pd
import os

# URL
url = os.getenv("MONGODB_URI")
# Create a client and connect to server
client = MongoClient(url)

# create a databse and collection 
DATABASE_NAME = "sensors"
COLLECTION_NAME = "waferfault"

# read csv file
df = pd.read_csv("D:\SensorProject\notebooks\wafer_23012020_041211.csv")

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)