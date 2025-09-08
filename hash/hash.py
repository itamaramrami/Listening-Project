import hashlib
from Loger_loges.loger import Logger_log


loger=Logger_log()

def get_hash(rout):
    try:
        hasher = hashlib.sha256()
        hasher.update(rout.encode('utf-8'))
        hash_id=hasher.hexdigest()
        loger.get_logger().info("get hash succeeded")
        return hash_id
    except Exception as e:
        print(f"get hash failed: {e}")
        loger.get_logger().error(f"get hash failed: {e}")
   
        
