import hashlib
import datetime

class Block:
    def __init__(self, data, previous_hash):
        # Create block for the blockchain using the SHA-256 encripting algorithm and the Greenwich Mean Time timestamp
        self.timestamp = datetime.datetime.now(datetime.timezone.utc)
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        # Calculate hash to encode information to store in the blockchain
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class LinkedList:
    # Create linked list class to function as a block chain with corresponding methods to add blocks
    def __init__(self):
        self.tail = None
        self.num_elements = 0

    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.size() == 0

    # Add block to block chain
    def append(self, data):
        if self.is_empty():
            block = Block(data, 0)
            self.tail = block
        
        previous = self.tail
        self.tail = Block(data, previous)
        self.num_elements += 1

    # List all blocks by data and timestamp
    def __repr__(self):
        if self.is_empty():
            return "The list is empty"
        s = ''
        current = self.tail
        while current.previous_hash:
            s += f'Block data: {current.data}, timestamp: {current.timestamp}\n'
            current = current.previous_hash
        return s


# Tests
# Add data to the linkedlist, then print it using the __repr__ function

# Test case 1
list = LinkedList()
list.append("This is the first block")
list.append("This is the second block")
list.append("This is the third block")
print(list)

# Test case 2
list2 = LinkedList()
list2.append("This is the another block")
list2.append("This is the second another block")
list2.append("This is the third anotherblock")
print(list2)

# Test case 3
list3 = LinkedList()
list3.append("Again")
list3.append("And again")
list3.append("And yet again")
print(list3)


        
