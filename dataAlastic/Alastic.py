from elasticsearch import Elasticsearch
from Loger_loges.loger import Logger_log





loger=Logger_log()

class Alastic:
    def __init__(self):
        try:
            self.es = Elasticsearch('http://localhost:9200')
            if not self.es.indices.exists(index="data_moazin"):
                self.es.indices.create(index="data_moazin")
            loger.get_logger().info("alastic connection succeeded")
        except Exception as e:
              print(f"alastic connection failed: {e}")
              loger.get_logger().error(f"alastic connection failed: {e}")
    
    def Loading_Data_Alastic(self,data):
            try:
                self.es.index(index='data_moazin', document=data)
                loger.get_logger().info("Loading Data alastic succeeded")
            except Exception as e:
                 print(f"Loading Data alastic failed: {e}")
                 loger.get_logger().error(f"Loading Data alastic failed: {e}")
    
    
    def GetData(self):
        res = self.es.search(
            index='data_moazin',
            query={"match_all": {}},
            size=1000
        )
        docs = [hit["_source"] for hit in res["hits"]["hits"]]
        return docs




