class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def __repr__(self):
        return str(self.get_value())

class LinkedList:
    # Create a linked list with the corresponding methods, focusing on adding elements
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.size() == 0

    # Prepend new items by offsetting the head
    def prepend(self, value):
        new_node = Node(value)
        self.num_elements += 1

        if self.is_empty():
            self.head = new_node
            return

        temp = self.head
        self.head = new_node
        new_node.next = temp

    def get_root(self):
        return self.head
        
    def __repr__(self):
        if self.is_empty():
            return 'There are no elements in the list'
        s = ''
        current = self.head
        while current:
            s += f'{str(current.get_value())}'
            if current.next:
                s += ' -> '
            current = current.next
        return s

def union(list_01, list_02):
    # Edge cases
    if list_01.is_empty() and list_02.is_empty():
        print('The lists are empty. There is no union')
        return

    # Create a new set and add all elements from both lists to the set
    union_set = set()

    first_current = list_01.get_root()
    while first_current:
        union_set.add(first_current.get_value())
        first_current = first_current.next

    second_current = list_02.get_root()
    while second_current:
        union_set.add(second_current.get_value())
        second_current = second_current.next
    
    # Add elements from the union set back to the list and return it
    linked_list = LinkedList()
    for value in union_set:
        linked_list.prepend(value)

    return linked_list

def intersection(list_01, list_02):
    # Edge cases
    if list_01.is_empty() or list_02.is_empty():
        print('Cannot make any intersection if one of the lists is empty')
        return

    # Create a temporary set and add elements from first list to the set
    temp_set = set()
    first_current = list_01.get_root()
    while first_current:
        temp_set.add(first_current.get_value())
        first_current = first_current.next

    # Create an intersection set. Go through second list elements. If they can be found in the temporary set, ad them to the intersection set
    intersection_set = set()
    second_current = list_02.get_root()
    while second_current:
        if second_current.get_value() in temp_set:
            intersection_set.add(second_current.get_value())
        second_current = second_current.next

    if(len(intersection_set) == 0):
        return 'There is no intersection between the lists provided'

    # Add elements from the intersection set back to the list and return it
    linked_list = LinkedList()
    for value in intersection_set:
        linked_list.prepend(value)

    return linked_list


# Tests
# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.prepend(i)

for i in element_2:
    linked_list_2.prepend(i)

print('First List:')
print(f'Union: {union(linked_list_1, linked_list_2)}')
print(f'Intersection: {intersection(linked_list_1, linked_list_2)}')

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.prepend(i)

for i in element_2:
    linked_list_4.prepend(i)

print('Second List:')
print(f'Union: {union(linked_list_3, linked_list_4)}')
print(f'Intersection: {intersection(linked_list_3, linked_list_4)}')
