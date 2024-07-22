# Longest Palindromic Subsequence

# In general, a palindrome is a string that reads the same backwards as forwards, e.g., MADAM.

# The Longest Palindromic Subsequence (LPS) is the most lengthy sequence of characters that is a palindrome.
# In this notebook, you'll be tasked with finding the length of the LPS in a given string of characters.

# Examples:
# 1. With an input string, MAXDYAM, the LPS is MADAM, which has length = 5
# 2. With an input string, BxAoNxAoNxA, the LPS is ANANA, which has length = 5
# 3. With an input string, BANANO, the LPS is NAN, which has length = 3
# 4. With an input string, ABBDBCACB, the LPS is BCACB, which has length = 5

## Solution

# imports for printing a matrix, nicely
import pprint
pp = pprint.PrettyPrinter()

# complete LPS solution
def lps(input_string): 
    n = len(input_string) 
  
    # create a lookup table to store results of subproblems 
    L = [[0 for x in range(n)] for x in range(n)] 
  
    # strings of length 1 have LPS length = 1
    for i in range(n): 
        L[i][i] = 1 
    
    # consider all substrings
    for s_size in range(2, n+1): 
        for start_idx in range(n-s_size+1): 
            end_idx = start_idx + s_size - 1
            if s_size == 2 and input_string[start_idx] == input_string[end_idx]:
                # match with a substring of length 2
                L[start_idx][end_idx] = 2
            elif input_string[start_idx] == input_string[end_idx]: 
                # general match case
                L[start_idx][end_idx] = L[start_idx+1][end_idx-1] + 2
            else:
                # no match case, taking the max of two values
                L[start_idx][end_idx] = max(L[start_idx][end_idx-1], L[start_idx+1][end_idx]); 
  
    # debug line
    # pp.pprint(L)
    
    return L[0][n-1] # value in top right corner of matrix

def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

def test():
    test_case_1 = ["BANANO", 3]
    test_function(test_case_1)

    test_case_2 = ["BxAoNxAoNxA", 5]
    test_function(test_case_2)

    test_case_3 = ["ABBDBCACB", 5]
    test_function(test_case_3)

    test_case_4 = ["MAXDYAM", 5]
    test_function(test_case_4)

if __name__ == "__main__":
    test()