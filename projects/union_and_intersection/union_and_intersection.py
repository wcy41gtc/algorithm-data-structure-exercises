# Your task for this problem is to fill out the union and intersection functions.
# The union of two sets A and B is the set of elements which are in A, in B, 
# or in both A and B. For example, the union of A = [1, 2] and B = [3, 4] is [1, 2, 3, 4].

# The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects 
# that are members of both sets A and B. For example, the intersection of A = [1, 2, 3] 
# and B = [2, 3, 4] is [2, 3].

# You will take in two linked lists and return a linked list that is composed of either 
# the union or intersection, respectively.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist1, llist2):
    union_set = set()
    current = llist1.head
    while current:
        union_set.add(current.value)
        current = current.next
    
    current = llist2.head
    while current:
        union_set.add(current.value)
        current = current.next
    
    sorted_union_set = sorted(union_set)
    union_llist = LinkedList()
    for value in sorted_union_set:
        union_llist.append(value)
    
    return union_llist

def intersection(llist1, llist2):
    set1 = set()
    current = llist1.head
    while current:
        set1.add(current.value)
        current = current.next
    
    intersection_set = set()
    current = llist2.head
    while current:
        if current.value in set1:
            intersection_set.add(current.value)
        current = current.next
    
    sorted_intersection_set = sorted(intersection_set)
    intersection_llist = LinkedList()
    for value in sorted_intersection_set:
        intersection_llist.append(value)
    
    return intersection_llist

def test():
    # Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]
    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)
    assert union(linked_list_1,linked_list_2).__str__() == "1 -> 2 -> 3 -> 4 -> 6 -> 9 -> 11 -> 21 -> 32 -> 35 -> 65 -> "
    assert intersection(linked_list_1,linked_list_2).__str__() == "4 -> 6 -> 21 -> "
    print("Test case 1 Passed")

    # Test case 2
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    element_1 = [1,2,3,4,5,6,7,8,9,10]
    element_2 = [1,2,3,4,5,6,7,8,9,10]
    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)
    
    assert union(linked_list_1,linked_list_2).__str__() == "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> "
    assert intersection(linked_list_1,linked_list_2).__str__() == "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> "
    print("Test case 2 Passed")

    # Test case 3
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    element_1 = [1,2,3,4,5,6,7,8,9,10]
    element_2 = [11,12,13,14,15,16,17,18,19,20]
    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)

    assert union(linked_list_1,linked_list_2).__str__() == "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> "
    assert intersection(linked_list_1,linked_list_2).__str__() == ""
    print("Test case 3 Passed")

    # Test case 4 (Empty linked list)
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    element_1 = []
    element_2 = []
    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)

    assert union(linked_list_1,linked_list_2).__str__() == ""
    assert intersection(linked_list_1,linked_list_2).__str__() == ""
    print("Test case 4 Passed")

    # Test case 5 (One Empty linked list)
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    element_1 = [1,2,3,4,5,6,7,8,9,10]
    element_2 = []
    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)

    assert union(linked_list_1,linked_list_2).__str__() == "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> "
    assert intersection(linked_list_1,linked_list_2).__str__() == ""
    print("Test case 5 Passed")

if __name__ == "__main__":
    test()