# twosum problem

# Varient 1: two sum with return true or false
# Problem: Given an array of integers, and a target value, return all pairs of numbers in the array that sum up to the target value

# Clarifying questions:
# 1. Are the numbers in the array sorted? Yes
# 2. Are there duplicate numbers in the array? Yes

# Plan:
# Brute force approach: iterate through the array and for each element, iterate through the rest of the array to see if they add up to the target value

# Time complexity: O(n^2), worst case
# Space complexity: O(1), only using a few variables.

# Implement
def two_sum_pairs(arr, target):
    pairs = set()
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.add((arr[i], arr[j]))
    return pairs

# Test cases with duplicate numbers
assert two_sum_pairs([1,2,3,4,4,4,5,6,7,8], 9) == set([(1, 8), (2, 7), (3, 6), (4, 5)])
assert two_sum_pairs([1,2,3,4,4,4,5,6,7,8], 10) == set([(2, 8), (3, 7), (4, 6)])
print("All test cases passed for the brute force approach")

# varient, return indices of the pairs

def two_sum_pairs_indices(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((i,j))
    return pairs

# Test cases with duplicate numbers
assert two_sum_pairs_indices([1,2,3,4,4,4,5,6,7,8], 9) == [(0, 9), (1, 8), (2, 7), (3, 6), (4, 6), (5, 6)]
assert two_sum_pairs_indices([1,2,3,4,4,4,5,6,7,8], 10) == [(1, 9), (2, 8), (3, 7), (4, 7), (5, 7)]
print("All test cases passed for the brute force approach")

# Optimized approach: using a hash table to store the elements we have seen so far

# Plan:
# create a hash table to store the elements and indices we have seen so far
# iterate through the array and for each element, check if the difference between the target and the element is in the hash table
# if it is, add the pair to the result

# Time complexity: O(n), worst case
# Space complexity: O(n), using a hash table to store the elements we have seen so far

# Implement
def two_sum_pairs_optimized1(arr, target):
    seen = {}
    pairs = []
    for i in range(len(arr)):
        if target - arr[i] in seen:
            for index in seen[target - arr[i]]:
                pairs.append((index, i))
        else:
            if arr[i] not in seen:
                seen[arr[i]] = [i]
            else:
                seen[arr[i]].append(i)
    return pairs

# Test cases with duplicate numbers
assert two_sum_pairs_optimized1([1,2,3,4,4,4,5,6,7,8], 9) == [(3, 6), (4, 6), (5, 6), (2, 7), (1, 8), (0, 9)]
assert two_sum_pairs_optimized1([1,2,3,4,4,4,5,6,7,8], 10) == [(3, 7), (4, 7), (5, 7), (2, 8), (1, 9)]
print("All test cases passed for the optimized approach 1")

# Optimized approach 2: using three pointers

# Plan:
# use three pointers, left, right, and i to iterate through the array, current starts as the same as left
# if the sum of the elements at left and right is less than the target, increment the left pointer
# if the sum is greater than the target, decrement the right pointer
# if the sum is equal to the target, add the pair to the result and increment the current pointer
# set a inner loop bewteen left and right pointers to check for duplicates, if there is any, add the pair to the result
# if the sum is greater than the target, decrement the right pointer

# Time complexity: O(n), worst case
# Space complexity: O(1), only using a few variables

# Implement

def two_sum_pairs_optimized2_right_to_left(arr, target):
    pairs = []
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            # check for duplicates
            for i in range(right, left, -1):
                if arr[i] == arr[right]:
                    pairs.append((left, i))
                else:
                    break
            left += 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return pairs

def two_sum_pairs_optimized2_left_to_right(arr, target):
    pairs = []
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            # check for duplicates
            for i in range(left, right):
                if arr[i] == arr[left]:
                    pairs.append((i, right))
                else:
                    break
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return pairs
# Test cases with duplicate numbers
print(two_sum_pairs_optimized2_right_to_left([1,2,3,4,4,4,5,6,7,8], 9))
print(two_sum_pairs_optimized2_left_to_right([1,2,3,4,4,4,5,6,7,8], 9))
assert two_sum_pairs_optimized2_right_to_left([1,2,3,4,4,4,5,6,7,8], 9) == [(0, 9), (1, 8), (2, 7), (3, 6), (4, 6), (5, 6)]
assert two_sum_pairs_optimized2_left_to_right([1,2,3,4,4,4,5,6,7,8], 9) == [(0, 9), (1, 8), (2, 7), (3, 6), (4, 6), (5, 6)]
print("All test cases passed for the optimized approach 2")

def two_sum_alternative(array, target):
    results = []
    left = 0
    right = len(array) - 1

    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target:
            # Include all pairs with the current left and equivalent rights
            for i in range(right, left, -1):
                if array[i] == array[right]:
                    results.append([left, i])
                else:
                    break
            left += 1  # Move left pointer to the next different element
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return results

print(two_sum_alternative([1,2,3,4,4,4,5,6,7,8], 9))