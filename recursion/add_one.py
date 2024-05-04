
# Problem Statement
# You are given a non-negative number in the form of list elements. For example, the number 123 would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list. 

# Example 1:
# input = [1, 2, 3]
# output = [1, 2, 4]

# Example 2:
# input = [1, 2, 9]
# output = [1, 3, 0]

# Example 3:
# input = [9, 9, 9]
# output = [1, 0, 0, 0]

def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    if arr == [9]:
        return [1, 0]
    if arr[-1] < 9:
        arr[-1] += 1
    else:
        arr = add_one(arr[:-1]) + [0]
    return arr

def test():
    # Test Cases
    print ("Pass" if  (add_one([0]) == [1]) else "Fail")
    print ("Pass" if  (add_one([1, 2, 3]) == [1, 2, 4]) else "Fail")
    print ("Pass" if  (add_one([9, 9, 9]) == [1, 0, 0, 0]) else "Fail")

if __name__ == '__main__':
    test()