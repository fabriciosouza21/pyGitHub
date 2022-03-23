import pymongo
class Connection:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["gitHub"]
        self.collection = self.db["issues"]

    
