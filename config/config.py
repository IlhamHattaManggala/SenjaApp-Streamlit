from pymongo import MongoClient

def get_db():
    uri = "mongodb+srv://capstonesmt6:capstonesmt6.25@senja-app.zut9mmt.mongodb.net/?retryWrites=true&w=majority&appName=Senja-App"
    client = MongoClient(uri, tls=True)
    db = client["senja"]
    return db

def get_collection(collection_name):
    db = get_db()
    return db[collection_name]
