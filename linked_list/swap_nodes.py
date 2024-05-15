class Node:
    """LinkedListNode class to be used for this problem"""
    def __init__(self, data):
        self.data = data
        self.next = None

# Solution
"""
:param: head- head of input linked list
:param: `position_one` - indicates position (index) ONE
:param: `position_two` - indicates position (index) TWO
return: head of updated linked list with nodes swapped
"""
def swap_nodes1(head, position_one, position_two):

    # If both the indices are same
    if position_one == position_two:
        return head
    
    # Helper references
    one_previous = None
    one_current = None

    two_previous = None
    two_current = None

    current_index = 0
    current_node = head 
    new_head = None

    # LOOP - find out previous and current node at both the positions (indices)
    while current_node is not None:
        
        # Position_one cannot be equal to position_two, 
        # so either one of them might be equal to the current_index
        if current_index == position_one:
            one_current = current_node
        
        elif current_index == position_two:
            two_current = current_node
            break

        # If neither of the position_one or position_two are equal to the current_index
        if one_current is None:
            one_previous = current_node
        
        two_previous = current_node
        
        # increment both the current_index and current_node
        current_node = current_node.next         
        current_index += 1
        

    # Loop ends
    
    
    '''SWAPPING LOGIC'''
    # We have identified the two nodes: one_current & two_current to be swapped, 
    # Make use of a temporary reference to swap the references
    two_previous.next = one_current
    temp = one_current.next
    one_current.next = two_current.next
    two_current.next = temp
    
    # if the node at first index is head of the original linked list
    if one_previous is None:
        new_head = two_current
    else:
        one_previous.next = two_current
        new_head = head
    # Swapping logic ends
    
    return new_head

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