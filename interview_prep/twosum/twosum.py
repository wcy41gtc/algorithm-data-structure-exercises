# twosum problem

# Varient 1: two sum with return true or false
# Problem: Given an array of integers, and a target value, return if there are two numbers in the array that sum up to the target value

# Clarifying questions:
# 1. Are the numbers in the array sorted? Yes
# 2. Are there duplicate numbers in the array? No

# Plan:
# brute force approach: iterate through the array and for each element, iterate through the rest of the array to see if they add up to the target value
# Time complexity: O(n^2), worst case
# Space complexity: O(1), only using a few variables.

# Implementing the brute force approach

def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False

# Test cases
assert two_sum([1, 2, 3, 4, 5], 9) == True
assert two_sum([1, 2, 3, 4, 5], 10) == False
print("All test cases passed for the brute force approach")

# Optimized approach: using a lookup table, a set, to store the elements we have seen so far

# Plan:
# iterate through the array and for each element, check if the difference between the target and the element is in the set
# if it is, return True

# Time complexity: O(n), worst case
# Space complexity: O(n), using a set to store the elements we have seen so far, worst case

# Implementing the optimized approach

def two_sum_optimized1(arr, target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return True
        seen.add(num)
    return False

# Test cases
assert two_sum_optimized1([1, 2, 3, 4, 5], 9) == True
assert two_sum_optimized1([1, 2, 3, 4, 5], 10) == False
print("All test cases passed for the optimized approach 1")

# Optimized approach 2: using two pointers, one at the beginning and one at the end of the array

# Plan:
# initialize two pointers, one at the beginning and one at the end of the array
# if the sum of the two pointers is equal to the target, return True
# if the sum is less than the target, increment the left pointer
# if the sum is greater than the target, decrement the right pointer

# Time complexity: O(n), worst case
# Space complexity: O(1), only using a

# Implementing the optimized approach 2

def two_sum_optimized2(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == target:
            return True
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    return False

# Test cases
assert two_sum_optimized2([1, 2, 3, 4, 5], 9) == True
assert two_sum_optimized2([1, 2, 3, 4, 5], 10) == False
print("All test cases passed for the optimized approach 2")



