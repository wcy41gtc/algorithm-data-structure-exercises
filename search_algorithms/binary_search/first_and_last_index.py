def first_and_last_index(arr, number):
    # search first occurence
    first_index = find_start_index(arr, number, 0, len(arr) - 1)
    
    # search last occurence
    last_index =  find_end_index(arr, number, 0, len(arr) - 1)
    return [first_index, last_index]


def find_start_index(arr, number, start_index, end_index):
    # binary search solution to search for the first index of the array
    if start_index > end_index:
        return -1

    mid_index = start_index + (end_index - start_index)//2

    if arr[mid_index] == number:
        current_start_pos = find_start_index(arr, number, start_index, mid_index - 1)
        if current_start_pos != -1:
            start_pos = current_start_pos
        else:
            start_pos = mid_index
        return start_pos

    elif arr[mid_index] < number:
        return find_start_index(arr, number, mid_index + 1, end_index)
    else:
        return find_start_index(arr, number, start_index, mid_index - 1)


def find_end_index(arr, number, start_index, end_index):
    # binary search solution to search for the last index of the array
    if start_index > end_index:
        return  -1

    mid_index = start_index + (end_index - start_index)//2

    if arr[mid_index] == number:
        current_end_pos = find_end_index(arr, number, mid_index + 1, end_index)
        if current_end_pos != -1:
            end_pos = current_end_pos
        else:
            end_pos = mid_index
        return end_pos
    elif arr[mid_index] < number:
        return find_end_index(arr, number, mid_index + 1, end_index)
    else:
        return find_end_index(arr, number, start_index, mid_index - 1)

def test_function(test_case):
    arr = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(arr, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

def test():
    arr = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
    number = 9
    solution = [6, 8]
    test_case = [arr, number, solution]
    test_function(test_case)

    arr = [100, 150, 150, 153]
    number = 150
    solution = [1, 2]
    test_case = [arr, number, solution]
    test_function(test_case)

    arr = [1, 2, 3, 4, 5, 6, 10]
    number = 9
    solution = [-1, -1]
    test_case = [arr, number, solution]
    test_function(test_case)

if __name__ == "__main__":
    test()
    