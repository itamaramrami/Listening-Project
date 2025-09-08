from pathlib import Path
from datetime import datetime

class Metadata:
    def __init__(self,path):
        self.file_path = Path(path)
        self.file_info = self.file_path.stat()
        self.file_name = self.file_path.name
        self.size = self.file_info.st_size
        self.time = self.file_info.st_ctime
        self.creation_date = datetime.fromtimestamp(self.time)
       
    
    
    def Create_json_for_metadat(self):
        data={
            "metadata":{
            "name":self.file_name,
            "size":self.size,
            "time":str(self.creation_date)},
            "path":str(self.file_path)
        }
        return data
        


# a=Metadata(r"C:\Users\IMOE001\Desktop\podcasts\download (1).wav")