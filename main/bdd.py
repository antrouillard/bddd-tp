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

#collection.delete_one({"COUNTRY":"GB"})
#collection.insert_one({"REFERENCE":"84.232.545","CURRENCY":"GBP","PRICE":12,"COUNTRY":"GB"})

searchCountry("GB")
searchCountry("FR")

client.close()