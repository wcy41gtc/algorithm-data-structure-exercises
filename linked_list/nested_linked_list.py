class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)
    
class LinkedList():
    def __init__(self, head):
        self.head = head
    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
    
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(int(str(node.value)))
            node = node.next
        return out

def merge(list1, list2):
    '''
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    '''
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    merged = LinkedList(None)
    while list1.head is not None or list2.head is not None:
        if list1.head is None:
            merged.append(list2.head.value)
            list2.head = list2.head.next
        elif list2.head is None:
            merged.append(list1.head.value)
            list1.head = list1.head.next
        elif list1.head.value <= list2.head.value:
            merged.append(list1.head.value)
            list1.head = list1.head.next
        else:
            merged.append(list2.head.value)
            list2.head = list2.head.next
    return merged

class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)
    
    def _flatten(self, node):
        if node.next is None:
            return merge(node.value, None)
        return merge(node.value, self._flatten(node.next))

class SortedLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        """
        Append a value to the Linked List in ascending sorted order

        Args:
           value(int): Value to add to Linked List
        """
        
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        if value < self.head.value:
            node = Node(value)
            node.next = self.head
            self.head = node
            return
        
        node = self.head
        while node.next is not None and value >= node.next.value:
            node = node.next
            
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node
        
        return None

def test():
    ''' Test merge() function'''
    linked_list = LinkedList(Node(1))
    linked_list.append(3)
    linked_list.append(5)

    second_linked_list = LinkedList(Node(2))
    second_linked_list.append(4)

    merged = merge(linked_list, second_linked_list)
    node = merged.head
    while node is not None:
        #This will print 1 2 3 4 5
        # print(type(node.value))
        print(node.value)
        node = node.next
        
    # Lets make sure it works with a None list
    merged = merge(None, linked_list)
    node = merged.head
    while node is not None:
        #This will print 1 3 5
        print(node.value)
        node = node.next
    ''' Test flatten() function'''
    # Create a nested linked list with one node. 
    # The node itself is a simple linked list as 1-->3-->5 created previously
    nested_linked_list = NestedLinkedList(Node(linked_list))

    # Append a node (a linked list as 2-->4) to the existing nested linked list
    nested_linked_list.append(second_linked_list)

    # Call the `flatten()` function
    flattened = nested_linked_list.flatten()

    # Logic to print the flattened list
    node = flattened.head
    while node is not None:
        #This will print 1 2 3 4 5
        print(node.value)
        node = node.next

    # Test cases
    linked_list = SortedLinkedList()
    linked_list.append(3)
    print ("Pass" if (linked_list.head.value == 3) else "Fail")

    linked_list.append(2)
    print ("Pass" if (linked_list.head.value == 2) else "Fail")

    linked_list.append(4)
    node = linked_list.head.next.next
    print ("Pass" if (node.value == 4) else "Fail")
if __name__ == '__main__':
    test()