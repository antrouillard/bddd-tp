import os
from pymongo import MongoClient

# Utilise une variable d'environnement pour l'URI MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

client = MongoClient(MONGO_URI)
db = client["assodb"]

def getGroupsID():
    collection = db["groupe"]
    result = collection.find()

    data = []
    for group in result:
        data.append([str(group["_id"]),group["NAME"]])

    print(data)
    return data