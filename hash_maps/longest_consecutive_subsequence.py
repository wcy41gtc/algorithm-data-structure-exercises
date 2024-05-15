# Problem Statement
# Given a list of integers that contain natural numbers in random order.  Write a program to find 
# the longest possible sub sequence of consecutive numbers in the array. Return this subsequence 
# in sorted order. 

# In other words, you have to return the sorted longest (sub) list of consecutive numbers present 
# anywhere in the given list. 

# For example, given the list [5, 4, 7, 10, 1, 3, 55, 2] the output should be [1, 2, 3, 4, 5]

# Note 
# 1. The solution must take O(n) time. Can you think of using a dictionary here?
# 2. If two subsequences are of equal length, return the subsequence whose index of smallest 
#    element comes first.

# The Idea:
# Every element of the given input_list could be a part of some subsequence. Therefore, we need a way 
# (using a dictionary) to keep track if an element has already been visited. Also, store length of a 
# subsequence if it is maximum. For this purpose, we have to check in forward direction, if the 
# (element+1) is available in the given dictionary, in a "while" loop. Similarly, we will check 
# in backward direction for (element-1), in another "while" loop. At last, if we have the smallest 
# element and the length of the longest subsequence, we can return a new list starting from 
# "smallest element" to "smallest element + length".

# The steps would be:
# 1. Create a dictionary, such that the elements of input_list become the "key", and the corresponding
#    index become the "value" in the dictionary. We are creating a dictionary because the lookup time is 
#    considered to be constant in a dictionary. 
# 2. For each element in the input_list, first mark it as visited in the dictionary
#  - Check in forward direction, if the (element+1) is available. If yes, increment the length of subsequence
#  - Check in backward direction, if the (element-1) is available. If yes, increment the length of subsequence
#  - Keep a track of length of longest subsequence visited so far. For the longest subsequence, store the 
#    smallest element (say start_element) and its index as well.  
# 3. Return a new list starting from start_element to start_element + length.

def longest_consecutive_subsequence(input_list):
    # Create a dictionary
    # key: element, value: index
    element_dict = dict()

    # Traverse through the input_list and populate the dictionary
    # Time complexity of this part is O(n)
    for index, element in enumerate(input_list):
        element_dict[element] = index

    # Variables to keep track of the length and starting element of the longest subsequence
    max_length = -1
    starts_at = -1

    # Traverse again - this time to find the actual sequences
    # Time complexity of this part is also O(n)
    for index, element in enumerate(input_list):

        current_starts = index
        element_dict[element] = -1  # Mark as visited

        current_count = 1  # length of the current subsequence

        '''CHECK ELEMENTS TO THE RIGHT'''
        current = element + 1

        # Check if the current element is the starting element of a subsequence
        while current in element_dict and element_dict[current] > 0:
            current_count += 1
            element_dict[current] = -1  # Mark as visited
            current = current + 1

        '''CHECK ELEMENTS TO THE LEFT'''
        current = element - 1

        # Check if the current element is the starting element of a subsequence
        while current in element_dict and element_dict[current] > 0:
            current_starts = element_dict[current]
            current_count += 1
            element_dict[current] = -1  # Mark as visited
            current = current - 1

        # Update optimal length and starting index of the subsequence
        if current_count >= max_length:
            if current_count == max_length and current_starts > starts_at:
                continue
            starts_at = current_starts
            max_length = current_count

    start_element = input_list[starts_at]
    return [element for element in range(start_element, start_element + max_length)]


def test_function(test_case):
    output = longest_consecutive_subsequence(test_case[0])
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")

def test():
    test_case_1 = [[5, 4, 7, 10, 1, 3, 55, 2], [1, 2, 3, 4, 5]]
    test_function(test_case_1)

    test_case_2 = [[2, 12, 9, 16, 10, 5, 3, 20, 25, 11, 1, 8, 6 ], [8, 9, 10, 11, 12]]
    test_function(test_case_2)

    test_case_3 = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
    test_function(test_case_3)

if __name__ == '__main__':
    test()