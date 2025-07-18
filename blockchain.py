import hashlib
import datetime

# Step 1: Create a Block class
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index                      # Block number
        self.timestamp = timestamp              # Time of creation
        self.data = data                        # Transaction data
        self.previous_hash = previous_hash      # Hash of previous block
        self.hash = self.calculate_hash()       # This block's own hash

    def calculate_hash(self):
        # Combine all values to generate hash
        block_contents = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(block_contents.encode()).hexdigest()
# Step 2: Create the first block (Genesis Block)
def create_genesis_block():
    return Block(0, datetime.datetime.now(), "Genesis Block", "0")

# Step 3: Initialize the blockchain list
blockchain = [create_genesis_block()]

# Step 4: Print the Genesis Block data
print("Genesis Block Created:")
print("Index:", blockchain[0].index)
print("Timestamp:", blockchain[0].timestamp)
print("Data:", blockchain[0].data)
print("Previous Hash:", blockchain[0].previous_hash)
print("Hash:", blockchain[0].hash)
