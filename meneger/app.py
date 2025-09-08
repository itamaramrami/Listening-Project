from conKafka.conkafka import kafka
from MetaData.data import Metadata
from list_path.pata import path

pub=kafka()
def mein():
    rout=path(r"C:\Users\IMOE001\Desktop\podcasts")
    list_of_path=rout.get_list()
    for row in list_of_path:
        data=Metadata(row)
        metadata=data.Create_json_for_metadat()
        pub.producer.send("metadata",metadata )
    pub.producer.flush()
    return   



if __name__=="__main__":
    mein()