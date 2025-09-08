from elasticsearch import Elasticsearch





class Alastic:
    def __init__(self):
        self.es = Elasticsearch('http://localhost:9200')
        self.es.indices.delete(index='metadata', ignore_unavailable=True)
        self.es.indices.create(index='metadata')
    
    def Loading_Data_Alastic(self,data):
                self.es.index(index='metadata', document=data)
                return

    def GetData(self):
        res = self.es.search(
            index='metadata',
            query={"match_all": {}},
            size=1000
        )
        docs = [hit["_source"] for hit in res["hits"]["hits"]]
        return docs
    
          
          
    





