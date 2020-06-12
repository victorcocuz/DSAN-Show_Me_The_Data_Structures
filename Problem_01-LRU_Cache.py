class Node:
# Create a Node class to count the use of each key
    def __init__(self, key):
        self.key = key
        self.used = 0
        self.next = None

class RecentlyUsed:
# Create a linked list to keep track of elements usage
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def add(self, key):
    # Add a new element to the list
        self.num_elements += 1
        if self.head is None:
            self.head = Node(key)
            return
        new_head = Node(key)
        new_head.next = self.head
        self.head = new_head
        # Swap elements so that even with no visits, the oldest added will be deleted first
        if self.head.next:
            self.swap_nodes(None, self.head)

    def increment(self, key):
    # Increment the usage value for the visited node
        node = self.head
        one_previous = None
        while node:
            if key == node.key:
                one_current = node
                one_current.used += 1
                self.swap_nodes(one_previous, one_current)
            one_previous = node
            node = node.next

    def swap_nodes(self, one_previous, one_current):
    # Swap nodes so that the one with most visits, or the newest one is always further from the head
        while one_current.next:
            if one_current.used >= one_current.next.used:
                two_current = one_current.next
                if one_previous is None:
                    self.head = two_current
                    one_previous = self.head
                else:
                    one_previous.next = two_current
                    one_previous = one_previous.next

                if one_current.next.next:
                    two_after = one_current.next.next
                else:
                    two_after = None

                two_current.next = one_current
                one_current.next = two_after
            else:
                break

    def remove_key(self, key):
        tail = self.head
        one_previous = None
        while tail:
            if key == tail.key:
                # one_current = tail
                self.swap_nodes(one_previous, tail.next)
            one_previous = tail
            tail = tail.next
        return key
        # return self.remove()

    def remove(self):
    # Remove the first node
        key = self.head.key
        self.head = self.head.next
        return key

    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0

    def __repr__(self):
    # List all the nodes in order
        if self.head is None:
            return 'Nothing has been added yet'
        node = self.head
        s = ''
        while node:
            s += (f'node key is {node.key} & node value is {node.used}\n')
            node = node.next
        return s


class LRU_Cache(object):
# Create a class for the cache
    def __init__(self, capacity):
        # Initialize class variables
        self.dict = {}
        self.capacity = capacity
        self.num_cached = 0
        self.recently_used = RecentlyUsed()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.dict:
            print(self.dict[key])
            self.recently_used.increment(key)
            return self.dict[key]
        else:
            print(-1)
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.num_cached == self.capacity:
            self.remove_lru()

        if key not in self.dict:
            self.recently_used.add(key)
        else:
            self.recently_used.remove_key(key)
            self.recently_used.add(key)

        self.dict[key] = value
        self.num_cached += 1
    
    def remove_lru(self):
        self.num_cached -= 1
        del self.dict[self.recently_used.remove()]

    # def __repr__(self):


# Test the cache implementation
first_cache = LRU_Cache(5)

first_cache.set(1, '1')
first_cache.set(2, '2')
first_cache.set(3, '3')
first_cache.set(4, '4')

first_cache.get(1)      # returns 1
first_cache.get(2)     # returns 2
first_cache.get(9)      # returns -1 because 9 is not present in the cache

first_cache.set(5, '5')
first_cache.set(6, '6')

# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
first_cache.get(3)

# Test edge case
first_cache.get(None)  # returns -1

# Check cache
first_cache.recently_used

# Test case
our_cache = LRU_Cache(3)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.get(4)   # Expected Value = 4
our_cache.get(1)   # Expected Value = -1
our_cache.set(2, 4)
our_cache.get(2)   # Expected Value = 4
our_cache.set(5, 5)
our_cache.get(3)   # Expected Value = -1
our_cache.get(5)   # Expected Value = 5
our_cache.set(2, 6)
our_cache.get(2)   # Expected Value = 6
our_cache.set(6, 6)
our_cache.get(4)   # Expected Value = -1
our_cache.get(6)   # Expected Value = 6
our_cache.set(5, 10)
our_cache.set(7, 7)
our_cache.get(2)   # Expected Value = -1 Your Output = 6
