def dutch_national_flag_sort(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1

    return arr

def test():
    assert dutch_national_flag_sort([1, 0]) == [0, 1]
    assert dutch_national_flag_sort([2, 1, 0]) == [0, 1, 2]
    assert dutch_national_flag_sort([2, 2, 0, 1, 2, 0]) == [0, 0, 1, 2, 2, 2]
    assert dutch_national_flag_sort([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]
    assert dutch_national_flag_sort([2, 0, 1]) == [0, 1, 2]
    assert dutch_national_flag_sort([2, 0, 1, 1, 0, 2]) == [0, 0, 1, 1, 2, 2]
    assert dutch_national_flag_sort([2, 0, 1, 1, 0, 2, 0, 1, 2]) == [0, 0, 0, 1, 1, 1, 2, 2, 2]
    print('All tests passed')

if __name__ == '__main__':
    test()