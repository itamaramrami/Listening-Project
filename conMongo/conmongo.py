from pymongo import MongoClient
import gridfs
uri = "mongodb://mongomes:27017"


class conMongo:
    def __init__(self, uri,db_name,col):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.fs =gridfs.GridFS(self.db)
        self.collection = self.db[col]
        

        
        
    def getCon(self):
        return self.collection