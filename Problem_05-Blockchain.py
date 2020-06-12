import hashlib
import datetime

class Block:
    def __init__(self, data, previous_hash):
        # Create block for the blockchain using the SHA-256 encripting algorithm and the Greenwich Mean Time timestamp
        self.timestamp = datetime.datetime.now(datetime.timezone.utc)
        self.data = data
        self.previous_hash = previous_hash
        self.previous = None
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
            self.tail = Block(data, 0)
        else:
            previous = self.tail
            self.tail = Block(data, previous.hash)
            self.tail.previous = previous

        self.num_elements += 1

    # List all blocks by data and timestamp
    def __repr__(self):
        if self.is_empty():
            return "The list is empty"
        s = ''
        current = self.tail
        while current:
            s += f'Block data: {current.data}, timestamp: {current.timestamp}, hash: {current.hash}\n'
            current = current.previous
        return s


# Tests
# Add data to the linkedlist, then print it using the __repr__ function

# Test case 1
list = LinkedList()
list.append("This is the first block")  # Prints data + time stamp
list.append("This is the second block")  # Prints data + time stamp
list.append("This is the third block")  # Prints data + time stamp
print(list)

# Test case 2
list2 = LinkedList()
list2.append("This is the another block")  # Prints data + time stamp
list2.append("This is the second another block")  # Prints data + time stamp
list2.append("This is the third anotherblock")  # Prints data + time stamp
print(list2)

# Test case 3
list3 = LinkedList()
list3.append("")  # Empty data, but adds timestamp
list3.append("")  # Empty data, but adds timestamp
list3.append("")  # Empty data, but adds timestamp
print(list3)


        
