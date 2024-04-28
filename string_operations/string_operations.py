# Exercise 1. Reverse Strings
# In this first exercise, the goal is to write a function that takes a string as input and then returns the reversed string.
# For example, if the input is the string "water", then the output should be "retaw".
# While you're working on the function and trying to figure out how to manipulate the string, it may help to use the print statement so you can see the effects of whatever you're trying.
# Note - You can use built-in method len() on the string.
def string_reverser(our_string):

    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    return our_string[::-1]

# Exercise 2. Anagrams
# The goal of this exercise is to write some code to determine if two strings are anagrams of each other.
# An anagram is a word (or phrase) that is formed by rearranging the letters of another word (or phrase).
# For example:
# "rat" is an anagram of "art"
# "alert" is an anagram of "alter"
# "Slot machines" is an anagram of "Cash lost in me"
# Your function should take two strings as input and return True if the two words are anagrams and False if they are not.
# You can assume the following about the input strings:
# No punctuation
# No numbers
# No special characters
# Note - You can use built-in methods len(), lower() and sort() on strings.

def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    
    stripped_str1 = sorted(str1.lower().replace(" ", ""))
    stripped_str2 = sorted(str2.lower().replace(" ", ""))
    
    return stripped_str1 == stripped_str2

# Exercise 3. Reverse the words in sentence
# Given a sentence, reverse each word in the sentence while keeping the order the same!

def word_flipper(our_string):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """
    
    flipped_string_list = []
    for word in our_string.split(" "):
        flipped_string_list.append(string_reverser(word))
    return " ".join(flipped_string_list)

# Exercise 4. Hamming Distance
# In information theory, the Hamming distance between two strings of equal length is the number of positions at which the corresponding symbols are different. Calculate the Hamming distace for the following test cases.
def hamming_distance(str1, str2):

    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """
    if len(str1) == len(str2):
        hamming_distance = 0
        for i, char in enumerate(str1):
            if char != str2[i]:
                hamming_distance += 1
        return hamming_distance
    else:
        return None
    
def main():
    # Test Cases for Exercise 1
    print ("Pass" if ('retaw' == string_reverser('water')) else "Fail")
    print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
    print ("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")
    # Test Cases for Exercise 2
    print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
    print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
    print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
    print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
    print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")
    # Test Cases for Exercise 3
    print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
    print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
    print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")
    # Test Cases for Exercise 4
    print ("Pass" if (10 == hamming_distance('ACTTGACCGGG','GATCCGGTACA')) else "Fail")
    print ("Pass" if  (1 == hamming_distance('shove','stove')) else "Fail")
    print ("Pass" if  (None == hamming_distance('Slot machines', 'Cash lost in me')) else "Fail")
    print ("Pass" if  (9 == hamming_distance('A gentleman','Elegant men')) else "Fail")
    print ("Pass" if  (2 == hamming_distance('0101010100011101','0101010100010001')) else "Fail")

if __name__ == "__main__":
    main()