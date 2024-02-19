from pymongo import MongoClient
from utils.envutil import Environment

env = Environment()


client = MongoClient(env.MONGO_URI)

