import hashlib


def get_hash(rout):
    hasher = hashlib.sha256()
    hasher.update(rout.encode('utf-8'))
    hash_id=hasher.hexdigest()
    return hash_id
   
        
