import hashlib
import datetime

class Block:
    
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(self.data)
      
    def calc_hash(self, data):
        sha = hashlib.sha256()

        hsh_str = str(data).encode('utf-8')

        sha.update(hsh_str)

        return sha.hexdigest()

    def __repr__(self):
        return str(self.hash)
    
class Blockchain:
    def __init__(self, last_block=None):
        self.last = last_block
    
    
    def insert(self, data):
        now = datetime.datetime.now()
        if self.last is None:
            new_block = Block(now.strftime("%m/%d/%Y, %H:%M:%S"), data, self.last)
            self.last = new_block
        new_block = Block(now.strftime("%m/%d/%Y, %H:%M:%S"), data, self.last)
        self.last = new_block
        return self.last.hash
    
    def view_only(self):
        cur_block = self.last
        out_dict = {}
        while cur_block:
            out_dict[cur_block.hash] = cur_block.timestamp
            cur_block = cur_block.previous_hash
        return out_dict
    


#  Test cases 
Blocked = Blockchain()
llist = [1, 3, 4, 5, 6]

for i in llist:
    Blocked.insert(i)
# 
print(Blocked.view_only())

