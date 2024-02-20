from pymongo import MongoClient
from utils.envutil import Environment

env = Environment()


client = MongoClient(env.MONGO_URI)

db = client["fastapi-mongo"]

user_collection= db["users"]
