from conKafka.conkafka import kafka
from MetaData.data import Metadata
from list_path.pata import path
from dataAlastic.Alastic import Alastic
from conMongo.conmongo import conMongo
from hash.hash import get_hash


con=kafka()
als=Alastic()
mon=conMongo("mongodb://localhost:27017","moazin","metadata")


def mein():
    rout=path(r"C:\Users\IMOE001\Desktop\podcasts")
    list_of_path=rout.get_list()
    for row in list_of_path:    
        data=Metadata(row)
        metadata=data.Create_json_for_metadat()
        con.producer.send("moazin_data",metadata)
    con.producer.flush()

    alldata=con.get_message()
    for data in alldata:
        dataa=data.value
        unique_identifier=get_hash(dataa["path"])
        metadata={"metadata":dataa,"hash_id":unique_identifier}
        als.Loading_Data_Alastic(metadata)
        row=dataa["path"]
        with open(row, "rb") as image_file:
            mon.fs.put(image_file,nique=unique_identifier)
        
        
    




    



if __name__=="__main__":
    mein()