import sys
import heapq

# Define the node class to handle each individual letter from the message together with its frequency
class Node:
    def __init__(self):
        self.value = 0
        self.freq = 0
        self.left = None
        self.right = None

    # Setters
    def set_value(self, value):
        self.value = value

    def set_freq(self, freq):
        self.freq = freq

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    # Getters
    def get_value(self):
        return self.value

    def get_freq(self):
        return self.freq
    
    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    # Checkers
    def has_left(self):
        return self.left != None

    def has_right(self):
        return self.right != None

    # Helpers
    def join_nodes(self, first_node, second_node, index):
        join_nodes = Node()
        join_nodes.set_value('IN' + str(index))
        join_nodes.set_left(first_node)
        join_nodes.set_right(second_node)
        join_nodes.set_freq(first_node.get_freq() + second_node.get_freq())
        return join_nodes

    # Traverse the node to encode message
    def get_letter_codes(self, node):
        letters = {}
        binary = []
        code = []
        def traverse(node):
            if node:
                if node.has_left():
                    binary.append('0')
                    traverse(node.get_left())
                if node.has_right():
                    binary.append('1')
                    traverse(node.get_right())
                if not (node.has_left() and node.has_right()):
                    result = ''
                    for char in binary:
                        result += char
                    letters[node.value] = result
                    code.extend(binary)
                if (len(binary) > 0):
                    binary.pop()
        traverse(node)
        return letters

    # Decode message by traversing the node
    def decode_message(self, data, node):
        initial_node = node
        message = ''
        for item in data:
            if item == '0':
                node = node.get_left()
            if item == '1':
                node = node.get_right()
            if not (node.has_left() and node.has_right()):
                message += node.get_value()
                node = initial_node
        return message

    # Repr
    def __repr__(self):
        s = 'The node contains the following children:\n'
        def traverse(node):
            if node is None:
                return ''
            s = ''
            s += f'{node.get_value()}\n'
            s += traverse(node.get_left())
            s += traverse(node.get_right())
            return s
        return s + traverse(self)

# Define a Priority Queue class to combine nodes selectively into a Huffman tree
class PriorityQueue:
    def __init__(self):
        self.array = []
        self.num_elements = 0

    def enqueue(self, node):
        # Add element on top of the queue
        self.array.append(node)
        self.num_elements += 1
    
    def dequeue(self):
        # Find node with smallest frequency and remove from the queue
        if self.is_empty():
            return

        min_node = None
        min_freq = 0
        for node in self.array:
            if min_node is None or node.freq < min_freq:
                min_node = node
                min_freq = node.get_freq()
        
        self.num_elements -= 1
        self.array.remove(min_node)
        return(min_node)

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.size() == 0

    # Print queue
    def __repr__(self):
        s = ''
        for node in self.array:
            left_value = None
            right_value = None
            if node.get_left() is not None:
                left_value = node.get_left().get_value()
            if node.get_right() is not None:
                right_value = node.get_right().get_value()
            s += f'Char: {node.get_value()}, freq: {node.get_freq()}, left value: {left_value}, right value: {right_value}\n'
        return s

# Encode Algorithm
def huffman_encoding(data):
    # Edge case
    if data is None:
        print('Cannot encode empty string')
        return None

    # Add all chars to a dictionary where key is character and value is frequency
    chars_freq = {}
    for char in data:
        chars_freq[char] = chars_freq.get(char, 0) + 1

    # Add all chars from dictionary to a queue
    queue = PriorityQueue()
    for char in chars_freq:
        node = Node()
        node.set_value(char)
        node.set_freq(chars_freq[char])
        queue.enqueue(node)

    # Add all nodes from the queue to a binary tree
    index = 0
    while queue.size() >= 2:
        queue.enqueue(Node().join_nodes(queue.dequeue(), queue.dequeue(), index))
        index += 1

    # Return all letters as a binary list
    tree = queue.dequeue()
    letters = Node().get_letter_codes(tree)
    code = ''
    for char in data:
        code += letters[char]
    return (code, tree)

# Decode Algorithm  
def huffman_decoding(data, tree):
    return Node().decode_message(data, tree)


# Test the encoding and decoding algorithms
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
