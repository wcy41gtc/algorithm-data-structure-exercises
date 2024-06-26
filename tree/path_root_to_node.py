# Problem Statement
# Given the root of a Binary Tree and a data value representing a node, 
# return the path from the root to that node in the form of a list. You 
# can assume that the binary tree has nodes with unique values.

class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
from queue import Queue

def convert_arr_to_binary_tree(arr):
    """
    Takes arr representing level-order traversal of Binary Tree 
    """
    index = 0
    length = len(arr)
    
    if length <= 0 or arr[0] == -1:
        return None

    root = BinaryTreeNode(arr[index])
    index += 1
    queue = Queue()
    queue.put(root)
    
    while not queue.empty():
        current_node = queue.get()
        left_child = arr[index]
        index += 1
        
        if left_child is not None:
            left_node = BinaryTreeNode(left_child)
            current_node.left = left_node
            queue.put(left_node)
        
        right_child = arr[index]
        index += 1
        
        if right_child is not None:
            right_node = BinaryTreeNode(right_child)
            current_node.right = right_node
            queue.put(right_node)
    return root


def path_from_root_to_node(root, data):
    """
    :param: root - root of binary tree
    :param: data - value (representing a node)
    """
    if root is None:
        return None

    if root.data == data:
        return [data]

    left_path = path_from_root_to_node(root.left, data)
    if left_path is not None:
        return [root.data] + left_path

    right_path = path_from_root_to_node(root.right, data)
    if right_path is not None:
        return [root.data] + right_path

    return None

def test_function(test_case):
    arr = test_case[0]
    data = test_case[1]
    solution = test_case[2]
    root = convert_arr_to_binary_tree(arr)
    output = path_from_root_to_node(root, data)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

def test():
    arr = [1, 2, 3, 4, 5, None, None, None, None, None, None]
    data = 5
    solution = [1, 2, 5]
    test_case = [arr, data, solution]
    test_function(test_case)

    arr = [1, 2, 3, 4, None, 5, None, None, None, None, None]
    data = 5
    solution = [1, 3, 5]
    test_case = [arr, data, solution]
    test_function(test_case)

    arr = [1, 2, 3, None, None, 4, 5, 6, None, 7, 8, 9, 10, None, None, None, None, None, None, 11, None, None, None]
    data = 8
    solution = [1, 3, 5,8]
    test_case = [arr, data, solution]
    test_function(test_case)

if __name__ == '__main__':
    test()