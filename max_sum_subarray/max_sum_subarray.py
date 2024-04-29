# Problem Statement

# You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within the input array.

# Example 1:
# arr= [1, 2, 3, -4, 6]
# The largest sum is 8, which is the sum of all elements of the array.

# Example 2:
# arr = [1, 2, -5, -4, 1, 6]
# The largest sum is 7, which is the sum of the last two elements of the array.

def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    current_sum = arr[0]
    max_sum = arr[0]
    for element in arr[1:]:
        current_sum = max(current_sum+element, element)
        max_sum = max(max_sum, current_sum)
    return max_sum

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

def test():
    arr = [1, 2, 3, -4, 6]
    solution = 8
    test_case = [arr, solution]
    test_function(test_case)

    arr = [1, 2, -5, -4, 1, 6]
    solution = 7
    test_case = [arr, solution]
    test_function(test_case)

    arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
    solution = 18
    test_case = [arr, solution]
    test_function(test_case)

if __name__ == '__main__':
    test()