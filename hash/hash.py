import hashlib

class hash_id:
    def __init__(self,rout):
        self.hasher = hashlib.sha256()
        self.hasher.update(rout.encode('utf-8'))
        self.hash_id=self.hasher.hexdigest()
    def get_hash(self):
        return self.hash_id
        
