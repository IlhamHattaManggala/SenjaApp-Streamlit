import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi

def get_db():
    uri = os.getenv("MONGO_URI")  # Ambil URI dari secrets
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print("Failed to connect to MongoDB:", e)
    db = client["senja"]
    return db

def get_collection(collection_name):
    db = get_db()
    return db[collection_name]
