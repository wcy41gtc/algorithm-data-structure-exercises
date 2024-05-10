## Problem statement
# Given an array arr and a target element target, find the last index of occurence 
# of target in arr using recursion. If target is not present in arr, return -1.
# For example:
# 1. For arr = [1, 2, 5, 5, 1, 2, 5, 4] and target = 5, output = 6
# 2. For arr = [1, 2, 5, 5, 1, 2, 5, 4] and target = 7, output = -1

def last_index(arr, target):
    return last_index_arr(arr, target, len(arr) - 1)
def last_index_arr(arr, target, index):
    if index < 0:
        return -1
    if arr[index] == target:
        return index
    return last_index_arr(arr, target, index - 1)

def test_function(test_case):
    arr = test_case[0]
    target = test_case[1]
    solution = test_case[2]
    output = last_index(arr, target)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

def test():
    arr = [1, 2, 5, 5, 1, 2, 5, 4]
    target = 5
    solution = 6
    test_case = [arr, target, solution]
    test_function(test_case)

    arr = [1, 2, 5, 5, 1, 2, 5, 4]
    target = 7
    solution = -1
    test_case = [arr, target, solution]
    test_function(test_case)

    arr = [91, 19, 3, 8, 9]
    target = 91
    solution = 0
    test_case = [arr, target, solution]
    test_function(test_case)

    arr = [1, 1, 1, 1, 1, 1]
    target = 1
    solution = 5
    test_case = [arr, target, solution]
    test_function(test_case)

if __name__ == '__main__':
    test()