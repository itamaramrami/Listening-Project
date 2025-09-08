from pymongo import MongoClient
import gridfs
from Loger_loges.loger import Logger_log


loger=Logger_log()

class conMongo:
    def __init__(self, uri,db_name,col):
        try:
            self.client = MongoClient(uri)
            self.db = self.client[db_name]
            self.fs =gridfs.GridFS(self.db)
            self.collection = self.db[col]
            loger.get_logger().info("mongo connection succeeded")
        except Exception as e:
            print(f"producer connection failed: {e}")
            loger.get_logger().error(f"producer connection failed: {e}")
            
    def getCon(self):
        return self.collection