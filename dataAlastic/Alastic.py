from elasticsearch import Elasticsearch
from Loger_loges.loger import Logger_log





loger=Logger_log()

class Alastic:
    def __init__(self):
        try:
            self.es = Elasticsearch('http://localhost:9200')
            self.es.indices.delete(index='metadata', ignore_unavailable=True)
            self.es.indices.create(index='metadata')
            loger.get_logger().info("alastic connection succeeded")
        except Exception as e:
              print(f"alastic connection failed: {e}")
              loger.get_logger().error(f"alastic connection failed: {e}")
    
    def Loading_Data_Alastic(self,data):
            try:
                self.es.index(index='metadata', document=data)
                loger.get_logger().info("Loading Data alastic succeeded")
                return
            except Exception as e:
                 print(f"Loading Data alastic failed: {e}")
                 loger.get_logger().error(f"Loading Data alastic failed: {e}")
    
    
    def GetData(self):
        res = self.es.search(
            index='metadata',
            query={"match_all": {}},
            size=1000
        )
        docs = [hit["_source"] for hit in res["hits"]["hits"]]
        return docs


a=Alastic()
print(a.GetData())

