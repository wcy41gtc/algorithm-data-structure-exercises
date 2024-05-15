# Problem statement
# Given an input_list and a target, return the pair of indices in the list 
# that holds the values which sum to the target. For example, 

# input_list = [1, 5, 9, 7] and target = 8, the answer would be [0, 3] 

# Note
# 1. The best solution takes O(n) time. This means that you cannot traverse 
# the given list more than once. Hint - Think of an additional data structure 
# that you should use here. 
# 2. You can assume that the list does not have any duplicates.

def pair_sum_to_target(input_list, target):
    # Create a dictionary
    # key: number
    # value: index of the number
    num_dict = {}
    
    for i in range(len(input_list)):
        num = input_list[i]
        diff = target - num
        
        # Check if the difference is in the dictionary
        if diff in num_dict:
            return [num_dict[diff], i]
        
        # Add the number to the dictionary
        num_dict[num] = i
    
    return None

def test_function(test_case):
    output = pair_sum_to_target(test_case[0], test_case[1])
    print(output)
    if sorted(output) == test_case[2]:
        print("Pass")
    else:
        print("Fail")

def test():
    test_case_1 = [[1, 5, 9, 7], 8, [0, 3]]
    test_function(test_case_1)

    test_case_2 = [[10, 5, 9, 7], 15, [0, 1]]
    test_function(test_case_2)

    test_case_3 = [[0, 8, 5, 7], 15, [1, 3]]
    test_function(test_case_3)

    test_case_4 = [[1, 5, 9, 7], 6, [0, 1]]
    test_function(test_case_4)

if __name__ == '__main__':
    test()