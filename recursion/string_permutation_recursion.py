# Problem Statement

# Given an input string, return all permutations of the string in an array.

# Example 1:
# string = 'ab'
# output = ['ab', 'ba']

# Example 2:
# string = 'abc'
# output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']

def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the string
    """

    permutationList = []


    if len(string) == 0:
        permutationList.append([])
    else:
        first_char = string[0]
        rest = string[1:]
        sub_permutationList = permutations(rest)
        for _ in sub_permutationList:
            if len(_) == 0:
                permutationList.append(first_char)
            else:
                for i in range(len(_)+1):
                    if i == 0:
                        permutationList.append(first_char + _)
                    elif i == len(_):
                        permutationList.append(_ + first_char)
                    else:
                        permutationList.append(_[:i] + first_char + _[i:])
    return permutationList


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")

def test():
    string = 'ab'
    solution = ['ab', 'ba']
    test_case = [string, solution]
    test_function(test_case)

    string = 'abc'
    solution = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
    test_case = [string, solution]
    test_function(test_case)

    string = 'abcd'
    solution = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
    test_case = [string, solution]
    test_function(test_case)

if __name__ == "__main__":
    test()