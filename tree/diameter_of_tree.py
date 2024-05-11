## Problem statement
# Given the root of a binary tree, find the diameter.
# Diameter of a Binary Tree is the maximum distance between any two nodes.
# The distance is measured by the number of edges between the two nodes.
# Diameter for a particular BinaryTree Node will be the maximum of:
# 1. Either diameter of left subtree
# 2. Or diameter of a right subtree
# 3. Or sum of left-height and right-height

class BinaryTreeNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
from queue import Queue

def convert_arr_to_binary_tree(arr):
    """
    Takes arr representing level-order traversal of Binary Tree 
    """
    index = 0
    length = len(arr)
    
    # check if the array is valid. If not, return None
    if length <= 0 or arr[0] == -1:
        return None

    # instantiate the root tree from the first element of the array
    root = BinaryTreeNode(arr[index])
    # increment the index of the array
    index += 1
    # instantiate a queue and add root node to the queue
    queue = Queue()
    queue.put(root)
    
    while not queue.empty():
        # get and remove the first element from the queue
        current_node = queue.get()
        # instantiate a left child from the array's current index
        left_child = arr[index]
        # move on to the next index
        index += 1
        
        if left_child is not None:
            # instantiate a binary tree node and append as left child
            left_node = BinaryTreeNode(left_child)
            current_node.left = left_node
            # add the left node to the queue
            queue.put(left_node)
        
        # instantiate the right child from the next element in the array
        right_child = arr[index]
        # move on to the next index
        index += 1
        
        if right_child is not None:
            # instantiate a binary tree node and append as left child
            right_node = BinaryTreeNode(right_child)
            current_node.right = right_node
            # add the right node to the queue
            queue.put(right_node)
            
    return root

def diameter_of_binary_tree(root):
    return diameter_of_binary_tree_func(root)[1]

def diameter_of_binary_tree_func(root):
    if root is None:
        return 0, 0
    
    left_height, left_diameter = diameter_of_binary_tree_func(root.left)
    right_height, right_diameter = diameter_of_binary_tree_func(root.right)
    
    current_height = max(left_height, right_height) + 1
    height_diameter = left_height + right_height
    current_diameter = max(left_diameter, right_diameter, height_diameter)
    
    return current_height, current_diameter

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    root = convert_arr_to_binary_tree(arr)
    output = diameter_of_binary_tree(root)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

def test():
    arr = [1, 2, 3, 4, 5, None, None, None, None, None, None]
    solution = 3
    test_case = [arr, solution]
    test_function(test_case)

    arr = [1, 2, 3, 4, None, 5, None, None, None, None, None]
    solution = 4
    test_case = [arr, solution]
    test_function(test_case)

    arr = [1, 2, 3, None, None, 4, 5, 6, None, 7, 8, 9, 10, None, None, None, None, None, None, 11, None, None, None]
    solution = 6

    test_case = [arr, solution]
    test_function(test_case)

if __name__ == '__main__':
    test()