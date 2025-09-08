from pathlib import Path
from datetime import datetime
from Loger_loges.loger import Logger_log

loger=Logger_log()

class Metadata:
    def __init__(self,path):
        self.file_path = Path(path)
        self.file_info = self.file_path.stat()
        self.file_name = self.file_path.name
        self.size = self.file_info.st_size
        self.time = self.file_info.st_ctime
        self.creation_date = datetime.fromtimestamp(self.time)
       
    
    
    def Create_json_for_metadat(self):
        try:
            data={
                "metadata":{
                "name":self.file_name,
                "size":self.size,
                "time":str(self.creation_date)},
                "path":str(self.file_path)
            }
            loger.get_logger().info("Create json for metadat succeeded")
            return data
        except Exception as e:
            print(f"Create json for metadat failed: {e}")
            loger.get_logger().error(f"Create json for metadat failed: {e}")
        


