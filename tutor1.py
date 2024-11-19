import hashlib
import datetime

class Block:
    def __init__(self,index,timestamp,data,previous_hash):
        self.index = index
        self.timestamp=timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(f'{self.index}{self.timestamp}{self.data}{self.previous_hash}'.encode()).hexdigest()
        

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0,datetime.datetime.now(), "Genesis Block", "0")
    
    def add_block(self,data):
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), datetime.datetime.now(), data, last_block.hash)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(f'Index: {block.index}, Data:{block.data}, Hash: {block.hash}')


# Blockchain oluştur ve blok ekle
blockchain = Blockchain()
blockchain.add_block("First block data")
blockchain.add_block("Second block data")
blockchain.print_chain()