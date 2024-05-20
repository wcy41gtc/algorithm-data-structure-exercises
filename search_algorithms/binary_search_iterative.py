def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration
   
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
   
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    lower_bound = 0
    upper_bound = len(array) - 1
    if upper_bound % 2 == 0:
        mid = int((lower_bound + upper_bound) / 2)
    else:
        mid = int((lower_bound + upper_bound - 1) / 2)
    if array[upper_bound] == target:
        return upper_bound
    if array[lower_bound] == target:
        return lower_bound
    while upper_bound - lower_bound > 1:
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            lower_bound = mid
            mid = int((lower_bound + upper_bound) / 2)
        else:
            upper_bound = mid
            mid = int((lower_bound + upper_bound) / 2)
    return None

def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")

def test():
    test_function([[0, 1, 2, 3, 4, 5, 6, 7], 6, 6])
    test_function([[0, 1, 2, 3, 4, 5, 6, 7], 0, 0])
    test_function([[0, 1, 2, 3, 4, 5, 6, 7], 3, 3])
    test_function([[0, 1, 2, 3, 4, 5, 6, 7], 7, 7])
    test_function([[0, 1, 2, 3, 4, 5, 6, 7], 8, None])
    test_function([[0, 1, 2, 3, 4, 5, 6, 7], -1, None])
    test_function([[0, 1, 2, 3, 4, 5, 6, 7], 1, 1])
    test_function([[0, 1, 2, 3, 4, 5, 6, 7], 5, 5])
    test_function([[0, 1, 2, 3, 4, 5, 6, 7], 4, 4])
    test_function([[0, 1, 2, 3, 4, 5, 6, 7], 2, 2])
    test_function([[0, 1, 2, 3, 4, 5, 6, 7], 9, None])
    test_function([[0, 1, 2, 3, 4, 5, 6, 7], -1, None])
    test_function([[0, 1, 2, 3, 4, 5, 6, 7], 8, None])
    test_function([[0, 1, 2, 3, 4, 5, 6, 7], 7, 7])
    test_function([[0, 1, 2, 3, 4, 5, 6, 7], 6, 6])

if __name__ == '__main__':
    test()