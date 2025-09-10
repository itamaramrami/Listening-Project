from elasticsearch import Elasticsearch
from Loger_loges.loger import Logger_log
import json





loger=Logger_log()

class Alastic:
    def __init__(self):
        try:
            self.es = Elasticsearch('http://localhost:9200')
            if not self.es.indices.exists(index="MetaData_Moazin"):
                self.es.indices.create(index="MetaData_Moazin")
            loger.get_logger().info("alastic connection succeeded")
        except Exception as e:
              print(f"alastic connection failed: {e}")
              loger.get_logger().error(f"alastic connection failed: {e}")
    
    def Loading_Data_Alastic(self,data):
            try:
                self.es.index(index='MetaData_Moazin', document=data)
                loger.get_logger().info("Loading Data alastic succeeded")
            except Exception as e:
                 print(f"Loading Data alastic failed: {e}")
                 loger.get_logger().error(f"Loading Data alastic failed: {e}")
    
    
    def GetData(self):
        res = self.es.search(
            index='MetaData_Moazin',
            query={"match_all": {}},
            size=1000
        )
        docs = [hit["_source"] for hit in res["hits"]["hits"]]
        return docs
    
    
    
    def update_data_id(self,name,nameparams,value):
        response = self.es.update_by_query(index="MetaData_Moazin",body={
            "query": {
                "match": {
                    "name":name
                }
            },
            "script": {
                "source": f"ctx._source.t= params.new_value",
                "params": {
                    nameparams:value
                }
            }
        })
    def get_data_text(self,name):
        response = self.es.search(index="MetaData_Moazin",body={
            "query": {
                "match": {
                    "name":name
                }
            }
            
        })
        docs = [hit["_source"] for hit in response["hits"]["hits"]]
        return docs[0]["text"]
        
        
    
    def get_name(self,hash):
        search_query = {
                "query": {
                    "term": {
                        "hash_id": hash
                            }
                            }
                        }
        response= self.es.search(index="MetaData_Moazin",body=search_query)
        docs = [hit["_source"] for hit in response["hits"]["hits"]]
        return docs[0]["name"]
    
    
    
    
    
    def get_data(self,hash):
        search_query = {
                "query": {
                    "term": {
                        "hash_id": hash
                            }
                            }
                        }
        response= self.es.search(index="MetaData_Moazin",body=search_query)
        docs = [hit["_source"] for hit in response["hits"]["hits"]]
        return docs[0]
        
        

