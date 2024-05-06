# Question - Let's use recursion to help us solve the following permutation problem:

# Given a list of items, the goal is to find all of the permutations of that list.
# For example, given a list like: [0, 1, 2] 
# Permutations: [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]] 
# Notice that the expected output is a list of permutation with each permuted item being 
# represented by a list. Such an object that contains other object is called "compound" object. 

# The Idea
# Build a compoundList incrementally starting with a blank list, and permute (add) each element 
# of original input list at all possible positions. 
# For example, take [0, 1, 2] as the original input list:
# 1. Start with a blank compoundList [[]]. This is actually the last call of recursive function
#    stack. Pick the element 2 of original input list, making the compoundList as [[2]]
# 2. Pick next element 1 of original input list, and add this element at position 0, and 1 for 
#    each list of previous compoundList. We will require to create copy of all lists of previous 
#    compoundList, and add the new element. Now, the compoundList will become [[1, 2], [2, 1]].
# 3. Pick next element 0 of original input list, and add this element at position 0, 1, and 2 for
#    each list of previous compoundList. Now, the compoundList will become 
#    [[0, 1, 2], [1, 0, 2], [1, 2, 0], [0, 2, 1], [2, 0, 1], [2, 1, 0]].

import copy

def permute(inputList):
    # a compound list
    finalCompoundList = []
    
    # a compound list
    compoundList = []
    
    # a blank list
    if len(inputList) == 0:
        finalCompoundList.append([])
        
    else:
        first_element = inputList[0] # pick the first element
        # the remaining list
        rest = inputList[1:]
        # recursive call
        compoundList = permute(rest)
        
        # iterate over compoundList
        for item in compoundList:
            for j in range(len(item)+1):
                # a copy of compoundList
                temp = copy.deepcopy(item)
                # insert the first element
                temp.insert(j, first_element)
                # append the list to finalCompoundList
                finalCompoundList.append(temp)
    return finalCompoundList

def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.
    
    Note that the ordering of the list is not important.
    
    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list
    
    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input
    
    o.sort()
    e.sort()
    return o == e

def test():
    input = [0, 1, 2]
    output = permute(input)
    expected_output = [ [0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0] ]
    assert check_output(output, expected_output) == True

    input = [0, 1]
    output = permute(input)
    expected_output = [ [0, 1], [1, 0] ]
    assert check_output(output, expected_output) == True

    input = [0]
    output = permute(input)
    expected_output = [ [0] ]
    assert check_output(output, expected_output) == True

    input = []
    output = permute(input)
    expected_output = [ [] ]
    assert check_output(output, expected_output) == True

    print("All test cases pass")

if __name__ == '__main__':
    test()