# Linked List Practice

# Implement a linked list class. You have to define a few functions that perform the desirbale action. Your `LinkedList` class should be able to:

# Append data to the tail of the list and prepend to the head
# Search the linked list for a value and return the node
# Remove a node
# Pop, which means to return the first node's value and delete the node from the list
# Insert data at some position in the list
# Return the size (length) of the linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out
    
    # Task 1. Write definition of `prepend()` function and test its functionality
    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        if self.head is None:
            self.head = Node(value)
            return
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    # Task 2. Write definition of `append()` function and test its functionality
    def append(self, value):
        """ Append a value to the end of the list. """
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
    # Task 3. Write definition of `search()` function and test its functionality
    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next
        return None
    # Task 4. Write definition of `remove()` function and test its functionality
    def remove(self, value):
        """ Remove first occurrence of value. """
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next
    # Task 5. Write definition of `pop()` function and test its functionality
    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        return node.value
    # Task 6. Write definition of `insert()` function and test its functionality
    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        if pos == 0:
            self.prepend(value)
            return
        index = 0
        node = self.head
        while node.next and index <= pos:
            if (pos - 1) == index:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return
            index += 1
            node = node.next
        else:
            self.append(value)
    # Task 7. Write definition of `size()` function and test its functionality
    def size(self):
        """ Return the size or length of the linked list. """
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size
    # Task 8. Write definition of 'reverse()' function and test its functionality
    def reverse(self):
        """ Reverse the linked list. """
        prev = None
        node = self.head
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        self.head = prev
    # Task 9. Write definition of `is_circular()` function and test its functionality
    def is_circular(self):
        """ Check if the linked list is circular. """
        if self.head is None:
            return False
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False