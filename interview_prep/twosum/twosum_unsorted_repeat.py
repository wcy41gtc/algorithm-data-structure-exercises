# Problem statement: Given an array of integers, and a target value, return all pairs of numbers in the array that sum up to the target value

# Clarifying questions:
# 1. Are the numbers in the array sorted? No
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
        if arr[i] in seen:
            seen[arr[i]].append(i)
        else:
            seen[arr[i]] = [i]
    return pairs

# Test cases with duplicate numbers
assert set(two_sum_pairs_optimized1([1,2,3,4,4,4,5,6,7,8], 9)) == set([(3, 6), (4, 6), (5, 6), (2, 7), (1, 8), (0, 9)])
assert set(two_sum_pairs_optimized1([1,2,3,4,4,4,5,6,7,8], 10)) == set([(1, 9), (2, 8), (3, 7), (4, 7), (5, 7)])
print("All test cases passed for the optimized approach")

# varient, return the pairs

def two_sum_pairs_optimized2(arr, target):
    seen = {}
    pairs = set()

    for i in range(len(arr)):
        if target - arr[i] in seen:
            for num in seen[target - arr[i]]:
                pairs.add((arr[i], num))
        if arr[i] in seen:
            seen[arr[i]].append(arr[i])
        else:
            seen[arr[i]] = [arr[i]]
    return list(pairs)

assert set(two_sum_pairs_optimized2([1,2,3,4,4,4,5,6,7,8], 9)) == set([(5, 4), (6, 3), (7, 2), (8, 1)])
assert set(two_sum_pairs_optimized2([1,2,3,4,4,4,5,6,7,8], 10)) == set([(8, 2), (6, 4), (7, 3)])
print("All test cases passed for the optimized approach 2")

