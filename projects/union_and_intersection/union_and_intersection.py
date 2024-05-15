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

def union(llist_1, llist_2):
    output = LinkedList()
    list1 = []
    list2 = []
    head1 = llist_1.head
    head2 = llist_2.head
    while head1 is not None:
        list1.append(head1.value)
        head1 = head1.next
    while head2 is not None:
        list2.append(head2.value)
        head2 = head2.next
    list1 = sorted(list(set(list1)))
    list2 = sorted(list(set(list2)))
    
    while True:
        if len(list1) == 0 and len(list2) == 0:
            break
        elif len(list1) == 0:
            output.append(list2.pop(0))
        elif len(list2) == 0:
            output.append(list1.pop(0))
        elif list1[0] < list2[0]:
            output.append(list1.pop(0))
        elif list1[0] > list2[0]:
            output.append(list2.pop(0))
        else:
            output.append(list1.pop(0))
            list2.pop(0)
    return output


def intersection(llist_1, llist_2):
    output = LinkedList()
    list1 = []
    list2 = []
    head1 = llist_1.head
    head2 = llist_2.head
    while head1 is not None:
        list1.append(head1.value)
        head1 = head1.next
    while head2 is not None:
        list2.append(head2.value)
        head2 = head2.next
    list1 = sorted(list(set(list1)))
    list2 = sorted(list(set(list2)))

    while True:
        if len(list1) == 0 or len(list2) == 0:
            break
        elif list1[0] < list2[0]:
            list1.pop(0)
        elif list1[0] > list2[0]:
            list2.pop(0)
        else:
            output.append(list1.pop(0))
            list2.pop(0)
    return output

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
    print (union(linked_list_1,linked_list_2)) # Expected output: 1 -> 2 -> 3 -> 4 -> 6 -> 9 -> 11 -> 21 -> 32 -> 35 -> 65 -> 
    print (intersection(linked_list_1,linked_list_2)) # Expected output: 4 -> 6 -> 21 -> 

    # Test case 2
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    element_1 = [1,2,3,4,5,6,7,8,9,10]
    element_2 = [1,2,3,4,5,6,7,8,9,10]
    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)
    print (union(linked_list_1,linked_list_2)) # Expected output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 
    print (intersection(linked_list_1,linked_list_2)) # Expected output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 

    # Test case 3
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    element_1 = [1,2,3,4,5,6,7,8,9,10]
    element_2 = [11,12,13,14,15,16,17,18,19,20]
    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)
    print (union(linked_list_1,linked_list_2)) # Expected output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 ->
    print (intersection(linked_list_1,linked_list_2)) # Expected output:

if __name__ == "__main__":
    test()