import os
from pymongo import MongoClient

# Utilise une variable d'environnement pour l'URI MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

client = MongoClient(MONGO_URI)
db = client["assodb"]