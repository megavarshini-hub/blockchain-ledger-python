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
import hashlib

# 1. Define a list to store the blockchain
blockchain = []

# 2. Define the function to create a block
def create_block(data, previous_hash):
    block_contents = data + previous_hash
    block_hash = hashlib.sha256(block_contents.encode()).hexdigest()
    block = {
        'data': data,
        'hash': block_hash,
        'previous_hash': previous_hash
    }
    return block

# 3. Create the Genesis block (first block manually)
genesis_block = create_block("Genesis Block", "0")
blockchain.append(genesis_block)

# 4. Function to add new blocks to the chain
def add_block(data):
    previous_block = blockchain[-1]  # Get last block
    new_block = create_block(data, previous_block['hash'])
    blockchain.append(new_block)

# 5. Add sample blocks
add_block("Mega sent 2 coins to Fathima")
add_block("Fathima sent 1 coin to Alex")

# 6. Validate the blockchain
def is_chain_valid():
    for i in range(1, len(blockchain)):
        current = blockchain[i]
        previous = blockchain[i-1]
        
        # Recalculate the hash of current block
        recalculated_hash = hashlib.sha256((current['data'] + current['previous_hash']).encode()).hexdigest()

        # Check if stored hash matches recalculated hash
        if current['hash'] != recalculated_hash:
            return False

        # Check if previous_hash matches
        if current['previous_hash'] != previous['hash']:
            return False
    return True

# 7. Print the blockchain
for block in blockchain:
    print(block)

# 8. Check if valid
print("Is blockchain valid?", is_chain_valid())
import hashlib
import time

# 🧱 Block structure
class Block:
    def __init__(self, index, previous_hash, transaction_data, timestamp):
        self.index = index
        self.previous_hash = previous_hash
        self.transaction_data = transaction_data
        self.timestamp = timestamp
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_contents = f"{self.index}{self.previous_hash}{self.transaction_data}{self.timestamp}"
        return hashlib.sha256(block_contents.encode()).hexdigest()

    def __str__(self):
        return f"""
        Block #{self.index}
        -------------------------
        Transaction : {self.transaction_data}
        Timestamp   : {self.timestamp}
        Prev Hash   : {self.previous_hash}
        Hash        : {self.hash}
        -------------------------
        """

# ⛓️ Blockchain structure
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block", time.time())

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transaction_data):
        latest_block = self.get_latest_block()
        new_index = latest_block.index + 1
        new_block = Block(new_index, latest_block.hash, transaction_data, time.time())
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(block)

# 🛠️ Let's test the blockchain
my_chain = Blockchain()
my_chain.add_block("Mega sent 10 coins to Fathima")
my_chain.add_block("Fathima sent 5 coins to Aishwarya")
my_chain.add_block("Aishwarya sent 2 coins to Ravi")

my_chain.print_chain()
import hashlib
import time

# Block structure
class Block:
    def __init__(self, index, previous_hash, transaction_data, timestamp):
        self.index = index
        self.previous_hash = previous_hash
        self.transaction_data = transaction_data
        self.timestamp = timestamp
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_contents = f"{self.index}{self.previous_hash}{self.transaction_data}{self.timestamp}"
        return hashlib.sha256(block_contents.encode()).hexdigest()

    def __str__(self):
        return f"""
        Block #{self.index}
        -------------------------
        Transaction : {self.transaction_data}
        Timestamp   : {self.timestamp}
        Prev Hash   : {self.previous_hash}
        Hash        : {self.hash}
        -------------------------
        """

# Blockchain structure
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block", time.time())

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transaction_data):
        latest_block = self.get_latest_block()
        new_index = latest_block.index + 1
        new_block = Block(new_index, latest_block.hash, transaction_data, time.time())
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]
            
            if curr.hash != curr.calculate_hash():
                print(f"Block {i} has been tampered!")
                return False
            if curr.previous_hash != prev.hash:
                print(f"Block {i} has wrong previous hash!")
                return False
        print("Blockchain is valid.")
        return True

    def print_chain(self):
        for block in self.chain:
            print(block)

# 🧪 Run the interactive demo
my_chain = Blockchain()

while True:
    choice = input("\nEnter transaction (or type 'done' to finish): ")
    if choice.lower() == 'done':
        break
    my_chain.add_block(choice)

print("\n🧾 Final Blockchain:\n")
my_chain.print_chain()

# ✅ Validate chain at end
print("\n🔒 Checking blockchain validity:")
my_chain.is_chain_valid()

