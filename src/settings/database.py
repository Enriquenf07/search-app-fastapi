from pymongo.mongo_client import MongoClient

client = MongoClient("localhost", 27017)

db = client.search_api

users = db["users"]



