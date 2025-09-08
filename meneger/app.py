from conKafka.conkafka import kafka
from MetaData.data import Metadata
from list_path.pata import path
from dataAlastic.Alastic import Alastic
from conMongo.conmongo import conMongo
from hash.hash import get_hash
from Loger_loges.loger import Logger_log



con=kafka()
als=Alastic()
mon=conMongo("mongodb://localhost:27017","moazin","metadata")
loger=Logger_log()


def mein():
    rout=path(r"C:\Users\IMOE001\Desktop\podcasts")
    list_of_path=rout.get_list()
    try:
        for row in list_of_path:    
            data=Metadata(row)
            metadata=data.Create_json_for_metadat()
            con.producer.send("moazin_metadata",metadata)
        con.producer.flush()
        alldata=con.get_message()
        loger.get_logger().info("metadata sent succeeded")
    except Exception as e:
        print(f"metadata sent failed: {e}")
        loger.get_logger().error(f"metadata sent failed: {e}")
    try:
        for data in alldata:
            dataa=data.value
            unique_identifier=get_hash(dataa["path"])
            metadata={"metadata":dataa,"hash_id":unique_identifier}
            als.Loading_Data_Alastic(metadata)
            row=dataa["path"]
            with open(row, "rb") as image_file:
                mon.fs.put(image_file,nique=unique_identifier)
            loger.get_logger().info("Loading data into Mongo + Alastic was successfully sent.")
    except Exception as e:
        print(f"Loading data into Mongo + Alastic was failed sent: {e}")
        loger.get_logger().error(f"Loading data into Mongo + Alastic was failed sent: {e}")
        
    




    



if __name__=="__main__":
    mein()