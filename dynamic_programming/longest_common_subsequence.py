# In text analysis, it is often useful to compare the similarity of two texts 
# (imagine if you were trying to determine plagiarism between a source and answer text). 
# In this notebook, we'll explore one measure of text similarity, the Longest Common Subsequence (LCS).

# The Longest Common Subsequence is the longest sequence of letters that are present in both the 
# given two strings in the same relative order.

# Example - Consider the two input strings, str1 = 'ABCD' and str2 = 'AXBXDX'. 
# The LCS will be 'ABD' with the length as 3 letters. 
# It is because each of the letters 'A' , 'B', and 'D' are present in both the given two strings in the same relative order.

# Note that:
# An LCS need not necessarily be a contiguous substring. 
# There can be more than one LCS present in the given two strings. 
# There can be many more common subsequences present here, with smaller length. 
# But, in this problem we are concerned with the longest common subsequence. 

def lcs(string_a, string_b):
    
    # initialize the matrix 
    lookup_table = [[0 for x in range(len(string_b) + 1)] for x in range(len(string_a) + 1)]
    
    # enumerate(str) returns a tuple containing the index and character in each iteration
    for char_a_i, char_a in enumerate(string_a):
        
        for char_b_i, char_b in enumerate(string_b):
            
            # If there is a match, 
            # fill that grid cell with the value to the top-left of that cell plus one
            if char_a == char_b:
                lookup_table[char_a_i + 1][char_b_i + 1] = lookup_table[char_a_i][char_b_i] + 1
                
            # If there is not a match, 
            # take the maximum value from either directly to the left or the top cell
            else:
                lookup_table[char_a_i + 1][char_b_i + 1] = max(
                    lookup_table[char_a_i][char_b_i + 1],
                    lookup_table[char_a_i + 1][char_b_i])

    # the bottom-right cell will hold the non-normalized LCS length value.
    return lookup_table[-1][-1]

def test():
    test_A1 = "WHOWEEKLY"
    test_B1 = "HOWONLY"

    lcs_val1 = lcs(test_A1, test_B1)

    test_A2 = "CATSINSPACETWO"
    test_B2 = "DOGSPACEWHO"

    lcs_val2 = lcs(test_A2, test_B2)

    assert lcs_val1==5, "Incorrect LCS value."
    assert lcs_val2==7, "Incorrect LCS value."
    print('Tests passed!')

if __name__ == '__main__':
    test()