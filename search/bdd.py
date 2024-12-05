from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
#client = MongoClient("mongodb://localhost:27020/")
db = client["assodb"]
user_collection = db["users"]

def searchUser(mail,hashed_password):
    resultats = user_collection.find({"MAIL":mail})

    for user in resultats[0:5]:
        print(user)

client.close()