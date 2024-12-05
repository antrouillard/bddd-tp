from pymongo import MongoClient
import time
client = MongoClient("mongodb://localhost:27017/")
#client = MongoClient("mongodb://localhost:27020/")
db = client["pricesdb"]
collection = db["prices"]

def searchCountry(country):
    start = time.time()
    resultats = collection.find({"COUNTRY":country})
    end = time.time()

    for doc in resultats[0:5]:
        print(doc)
    
    print(f"Search done in {end-start:.30f}sec")


client.close()