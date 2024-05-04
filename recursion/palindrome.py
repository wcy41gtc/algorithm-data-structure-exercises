# A palindrome is a word that is the reverse of itself—that is, 
# it is the same word when read forwards and backwards.

# For example:
# "madam" is a palindrome
# "abba" is a palindrome
# "cat" is not
# "a" is a trivial case of a palindrome

# The goal of this exercise is to use recursion to write a function is_palindrome()
# that takes a string as input and checks whether that string is a palindrome. 
# (Note that this problem can also be solved with a non-recursive solution, 
# but that's not the point of this exercise.)

def is_palindrome(input_string):
    """
    Check if a string is a palindrome using recursion
    Args:
       input_string(string): Input string to be checked if it is a palindrome
    Returns:
       bool: True if string is palindrome, False otherwise
    """
    if len(input_string) == 0:
        return True
    else:
        first_char = input_string[0]
        last_char = input_string[-1]
        the_rest = slice(1, -1)
        sub_string = input_string[the_rest]
        return (first_char == last_char) and is_palindrome(sub_string)
    
def test():
    # Test Cases
    print ("Pass" if  (is_palindrome("")) else "Fail")
    print ("Pass" if  (is_palindrome("a")) else "Fail")
    print ("Pass" if  (is_palindrome("madam")) else "Fail")
    print ("Pass" if  (is_palindrome("abba")) else "Fail")
    print ("Pass" if not (is_palindrome("Udacity")) else "Fail")
    print ("Pass" if not (is_palindrome("I am not a robot")) else "Fail")

if __name__ == '__main__':
    test()