import os
from Loger_loges.loger import Logger_log


loger=Logger_log()

class path:
    def __init__(self,directory_path):
        try:
            self.all_paths = []
            for root, dirs, files in os.walk(directory_path):
                for name in files:
                    self.all_paths.append(os.path.join(root, name))
                for name in dirs:
                    self.all_paths.append(os.path.join(root, name))
            loger.get_logger().info("get list of paths succeeded")
        except Exception as e:
            print(f"get list of paths failed: {e}")
            loger.get_logger().error(f"get list of paths failed: {e}")
    
    def get_list(self):
        return self.all_paths
