def reverse_string(input_string):
    """
    Reverse a string using recursion
    Args:
       input_string(string): string to be reversed
    Returns:
       a string that is the reverse of input_string
    """
    if len(input_string) == 0:
        return ""
    else:
        first_char = input_string[0]
        the_rest = slice(1, None)
        sub_string = input_string[the_rest]
        reversed_substring = reverse_string(sub_string)
        return reversed_substring + first_char
    

def test():
    # Test Cases
    print ("Pass" if  ("" == reverse_string("")) else "Fail")
    print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")
    print ("Pass" if  ("I am not a robot" == reverse_string("tobor a ton ma I")) else "Fail")

if __name__ == '__main__':
    test()