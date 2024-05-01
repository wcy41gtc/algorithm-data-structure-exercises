class Node:
    """LinkedListNode class to be used for this problem"""
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_nodes1(head, left_index, right_index):
    """
    Swaps the nodes at the given indices in the linked list.
    """
    # Create a dummy node to point to the head of the linked list
    dummy = Node(0)
    dummy.next = head

    # Initialize the previous node to the dummy node
    prev = dummy

    # Traverse the linked list to find the left and right nodes
    for _ in range(left_index):
        prev = prev.next
    left = prev.next

    for _ in range(right_index - left_index):
        prev = prev.next
    right = prev.next

    # Swap the left and right nodes
    prev.next = left
    left.next, right.next = right.next, left.next
    right.next = left

    return dummy.next

# My solution:
def swap_nodes(head, left_index, right_index):
    if left_index == 0 and right_index == 0:
        return head
    if left_index >= right_index:
        return head
    
    one_prev = None
    one_current = head
    one_next = None
    two_prev = None
    two_current = None
    
    for _ in range(left_index):
        one_prev = one_current
        one_current = one_current.next
        one_next = one_current.next
    two_current = one_current
    two_prev = one_prev
    for _ in range(right_index-left_index):
        two_prev = two_current
        two_current = two_current.next
    if right_index - left_index == 1 and left_index != 0:
        temp = two_current.next
        two_current.next = one_current
        one_prev.next = two_current
        one_current.next = temp
        return head
    elif right_index - left_index != 1 and left_index == 0:
        temp1 = one_current.next
        temp2 = two_current.next
        two_current.next = temp1
        one_current.next = temp2
        two_prev.next = one_current
        return two_current
    elif right_index - left_index == 1 and left_index == 0:
        temp1 = two_current.next
        two_current.next = one_current
        one_current.next = temp1
        return two_current
    else:
        temp = two_current.next
        two_current.next = one_next
        one_prev.next = two_current
        two_prev.next = one_current
        one_current.next = temp
        return head
    
def test_function(test_case):
    head = test_case[0]
    left_index = test_case[1]
    right_index = test_case[2]
    
    left_node = None
    right_node = None
    
    temp = head
    index = 0
    try:
        while temp is not None:
            if index == left_index:
                left_node = temp
            if index == right_index:
                right_node = temp
                break
            index += 1
            temp = temp.next

        updated_head = swap_nodes(head, left_index, right_index)

        temp = updated_head
        index = 0
        pass_status = [False, False]

        while temp is not None:
            if index == left_index:
                pass_status[0] = temp is right_node
            if index == right_index:
                pass_status[1] = temp is left_node

            index += 1
            temp = temp.next

        if pass_status[0] and pass_status[1]:
            print("Pass")
        else:
            print("Fail")
        return updated_head
    except Exception as e:
        print("Fail")

# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next

def test():
    arr = [3, 4, 5, 2, 6, 1, 9]
    head = create_linked_list(arr)
    left_index = 3
    right_index = 4
    test_case = [head, left_index, right_index]
    updated_head = test_function(test_case)

    arr = [3, 4, 5, 2, 6, 1, 9]
    left_index = 2 
    right_index = 4
    head = create_linked_list(arr)
    test_case = [head, left_index, right_index]
    updated_head = test_function(test_case)

    arr = [3, 4, 5, 2, 6, 1, 9]
    left_index = 0
    right_index = 1
    head = create_linked_list(arr)
    test_case = [head, left_index, right_index]
    updated_head = test_function(test_case)

if __name__ == "__main__":
    test()