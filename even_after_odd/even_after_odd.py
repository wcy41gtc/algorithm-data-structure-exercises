# Problem Statement

# Given a linked list with integer data, arrange the elements in such a manner that all nodes 
# with even numbers are placed after odd numbers. Do not create any new nodes and avoid using
# any other data structure. The relative order of even and odd elements must not change.

# Example:
# linked list = 1 2 3 4 5 6
# output = 1 3 5 2 4 6

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def even_after_odd(head):
    if head is None:
        return head

    odd = None
    even = None
    odd_tail = None
    even_tail = None

    while head:
        next_node = head.next
        head.next = None

        if head.data % 2 == 0:
            if even is None:
                even = head
                even_tail = head
            else:
                even_tail.next = head
                even_tail = even_tail.next
        else:
            if odd is None:
                odd = head
                odd_tail = head
            else:
                odd_tail.next = head
                odd_tail = odd_tail.next

        head = next_node

    if odd is None:
        return even

    odd_tail.next = even
    return odd

def test():
    # Test case 1
    # linked list = 1 2 3 4 5 6
    # output = 1 3 5 2 4 6
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head = even_after_odd(head)
    assert head.data == 1
    assert head.next.data == 3
    assert head.next.next.data == 5
    assert head.next.next.next.data == 2
    assert head.next.next.next.next.data == 4
    assert head.next.next.next.next.next.data == 6

    # Test case 2
    # linked list = 1 3 5 7 9
    # output = 1 3 5 7 9
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(5)
    head.next.next.next = Node(7)
    head.next.next.next.next = Node(9)

    head = even_after_odd(head)
    assert head.data == 1
    assert head.next.data == 3
    assert head.next.next.data == 5
    assert head.next.next.next.data == 7
    assert head.next.next.next.next.data == 9

    # Test case 3
    # linked list = 2 4 6 8 10
    # output = 2 4 6 8 10
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    head = even_after_odd(head)
    assert head.data == 2
    assert head.next.data == 4
    assert head.next.next.data == 6
    assert head.next.next.next.data == 8
    assert head.next.next.next.next.data == 10

if __name__ == '__main__':
    test()
    print('All test cases pass')