import hashlib
import time


class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calc_hash()
    
    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update((str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.data)).encode('utf-8'))
        return sha.hexdigest()

class BlockChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block")
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(latest_block.index + 1, latest_block.hash, time.time(), data)
        self.chain.append(new_block)
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            if current_block.hash != current_block.calc_hash():
                print(f"Current block hash invalid: {current_block.hash} != {current_block.calc_hash()}")
                return False
            
            if current_block.previous_hash != previous_block.hash:
                print(f"Previous block hash invalid: {current_block.previous_hash} != {previous_block.hash}")
                return False
        
        return True

def test():
    # Test Case 1: Regular Input
    blockchain = BlockChain()
    blockchain.add_block("Block 1")
    blockchain.add_block("Block 2")
    blockchain.add_block("Block 3")
    assert blockchain.is_chain_valid(), "Test Case 1 Failed"
    print("Test Case 1 Passed")
    
    # Test Case 2: Empty Input (Edge Case)
    blockchain = BlockChain()
    blockchain.add_block("")
    assert blockchain.is_chain_valid(), "Test Case 2 Failed"
    print("Test Case 2 Passed")
    
    # Test Case 3: Very Large Input (Edge Case)
    blockchain = BlockChain()
    blockchain.add_block("A" * 10**6)
    assert blockchain.is_chain_valid(), "Test Case 3 Failed"
    print("Test Case 3 Passed")

if __name__ == "__main__":
    test()