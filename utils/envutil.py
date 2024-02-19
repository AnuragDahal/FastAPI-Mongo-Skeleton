from dotenv import load_dotenv
import os

load_dotenv()


class Environment():
    def __init__(self):
        self.MONGO_URI = os.getenv("MONGO_URI")
