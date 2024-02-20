from pymongo import MongoClient
from utils.envutil import Environment

env = Environment()


client = MongoClient(env.MONGO_URI)

db = client["fastapi-mongo"]
collection_name = db["users"]


def create(collection):
    db.create_collection(collection)
