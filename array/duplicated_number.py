# Problem Statement

# You have been given an array of length = n. The array contains integers from 0 to n - 2. Each number in the array is present exactly once except for one number which is present twice. Find and return this duplicate number present in the array

# Example:
# arr = [0, 2, 3, 1, 4, 5, 3]
# output = 3 (because 3 is present twice)

# The expected time complexity for this problem is O(n) and the expected space-complexity is O(1).


'''
Notice carefully that
1. All the elements of the array are always non-negative
2. If array length = n, then elements would start from 0 to (n-2), i.e. Natural numbers 0,1,2,3,4,5...(n-2)
3. There is only SINGLE element which is present twice.

Therefore let's find the sum of all elements (current_sum) of the original array, and
find the sum of first (n-2) Natural numbers (expected_sum).

Trick: 
The second occurance of a particular number (say `x`) is actually occupying the space 
that would have been utilized by the number (n-1). This leads to: 
current_sum  = 0 + 1 + 2 + 3 + .... + (n-2) + x
expected_sum = 0 + 1 + 2 + 3 + .... + (n-2)
current_sum - expected_sum = x 
Tada!!! :)  

'''
def duplicate_number(arr):
    current_sum = 0
    expected_sum = (len(arr)-2)*(len(arr)-1)/2
    
    for num in arr:
        current_sum += num
    return current_sum - expected_sum

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

def test():
    arr = [0, 2, 3, 1, 4, 5, 3]
    solution = 3
    test_case = [arr, solution]
    test_function(test_case)

    arr = [0, 1, 5, 4, 3, 2, 0]
    solution = 0
    test_case = [arr, solution]
    test_function(test_case)

if __name__ == '__main__':
    test()

