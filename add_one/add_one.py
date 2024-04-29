# Problem Statement

# You are given a non-negative number in the form of list elements. For example, the number `123` would be provided as `arr = [1, 2, 3]`. Add one to the number and return the output in the form of a new list. 

# Example 1:
# input = [1, 2, 3]
# output = [1, 2, 4]


# Example 2:
# input = [1, 2, 9]
# output = [1, 3, 0]

# Example 3:
# input = [9, 9, 9]
# output = [1, 0, 0, 0]


# Challenge:
# One way to solve this problem is to convert the input array into a number and then add one to it. For example, if we have `input = [1, 2, 3]`, you could solve this problem by creating the number `123` and then separating the digits of the output number `124`.

# But can you solve it in some other way?

def add_one_sol1(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    # Convert the list to a string
    num = ''.join(map(str, arr))
    # Convert the string to an integer, add 1 to it and convert it back to a string
    num = str(int(num) + 1)
    # Convert the string to a list
    return [int(i) for i in num]

def add_one_sol2(arr):
    """
    The Logic
    1. The idea is to start checking the array from the right end, in a FOR loop. 
    2. Add 1 to the digit, and check if it lies in the range 0-9 OR becomes 10.
    3. If the updated digit is between 0-9, quit the FOR loop. (Example, original array is [1,2,3])
    4. Otherwise update the current position in the array, and carry over the "borrow" to the next left digit. (Example, original array is [9,9,9])
    5. Once, we finish iteratig over all the digits of the original array, we will be left with the final "borrow", either 0 or 1. Prepend this "borrow" to the original array. 
    6. Return the updated array, but there is trick which helps us to select the starting index of the updated array. Example, [0, 1, 2, 4] is the updated array, and we want to return only [1, 2, 4]
    """
    borrow = 1
    for i in range(len(arr), 0, -1):
        digit = borrow + arr[i - 1]
        borrow = digit // 10
        if borrow == 0:
            arr[i - 1] = digit
            break
        else:
            arr[i - 1] = digit % 10
    arr = [borrow] + arr if borrow else arr
    # Find the position of the first non-zero digit
    position = 0
    while arr[position] == 0:
        position += 1
    return arr[position:]

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = add_one_sol2(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")   

def test():
    # Test case 1
    arr = [1, 2, 3]
    solution = [1, 2, 4]
    test_case = [arr, solution]
    test_function(test_case)
    # Test case 2
    arr = [1, 2, 9]
    solution = [1, 3, 0]
    test_case = [arr, solution]
    test_function(test_case)
    # Test case 3
    arr = [9, 9, 9]
    solution = [1, 0, 0, 0]
    test_case = [arr, solution]
    test_function(test_case)

if __name__ == "__main__":
    test()