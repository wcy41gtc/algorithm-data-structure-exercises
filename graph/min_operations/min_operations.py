# Starting from the number 0, find the minimum number of operations required to reach a given positive 
# target number. You can only use the following two operations:

# 1. Add 1
# 2. Double the number
    
# ### Example:

# 1. For Target = 18,  output = 6, because it takes at least 6 steps shown below to reach the target

#   start = 0
#   step 1 ==> 0 + 1 = 1
#   step 2 ==> 1 * 2 = 2  or 1 + 1 = 2
#   step 3 ==> 2 * 2 = 4
#   step 4 ==> 4 * 2 = 8
#   step 5 ==> 8 + 1 = 9
#   step 6 ==> 9 * 2 = 18

 

# 2. For Target = 69, output = 9, because it takes at least 8 steps to reach 69 from 0 using the allowed operations

#   start = 0
#   step 1 ==> 0 + 1 = 1
#   step 2 ==> 1 + 1 = 2
#   step 3 ==> 2 * 2 = 4
#   step 4 ==> 4 * 2 = 8
#   step 5 ==> 8 * 2 = 16
#   step 6 ==> 16 + 1 = 17
#   step 7 ==> 17 * 2 = 34
#   step 8 ==> 34 * 2 = 68
#   step 9 ==> 68 + 1  = 69




from collections import deque
def min_operations(target):
    if target == 0:
        return 0

    queue = deque([(0, 0)])  # (current number, steps taken)
    visited = set()

    while queue:
        current, steps = queue.popleft()

        # Check the two possible operations
        next_add = current + 1
        next_double = current * 2

        # If we reach the target with either operation, return the steps
        if next_add == target or next_double == target:
            return steps + 1

        # Add next_add to the queue if it has not been visited and is <= target
        if next_add <= target and next_add not in visited:
            visited.add(next_add)
            queue.append((next_add, steps + 1))

        # Add next_double to the queue if it has not been visited and is <= target
        if next_double <= target and next_double not in visited:
            visited.add(next_double)
            queue.append((next_double, steps + 1))

def test():
    # Test case 1
    target = 18
    assert min_operations(target) == 6

    # Test case 2
    target = 69
    assert min_operations(target) == 9

    # Test case 3
    target = 1024
    assert min_operations(target) == 11

    # Test case 4
    target = 1
    assert min_operations(target) == 1

    # Test case 5
    target = 0
    assert min_operations(target) == 0

    print("All test cases pass")

if __name__ == "__main__":
    test()