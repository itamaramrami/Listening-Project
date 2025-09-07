from pub.producer import kafka
from MetaData.data import Metadata
from list_path.pata import path
import json

pub=kafka()
def mein():
    rout=path(r"C:\Users\IMOE001\Desktop\podcasts")
    list_of_path=rout.get_list()
    for i in range(len(list_of_path)-1):
        data=Metadata(r"C:\Users\IMOE001\Desktop\podcasts\download (2).wav")
        metadata=data.Create_json_for_metadat()
        pub.producer.send("messages",metadata )
    return   



if __name__=="__main__":
    mein()