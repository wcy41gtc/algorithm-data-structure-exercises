def search_rotated_array(arr, key):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid
        # determine which side of the array is sorted
        if arr[start] <= arr[mid]: # left side is sorted
            if arr[start] <= key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else: # right side is sorted
            if arr[mid] < key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1

def test():
    assert search_rotated_array([10, 15, 1, 3, 8], 15) == 1
    assert search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10) == 4
    assert search_rotated_array([4, 5, 7, 9, 10, -1, 2], 6) == -1
    assert search_rotated_array([1, 3, 8, 10, 15], 10) == 3
    assert search_rotated_array([1, 3, 8, 10, 15], 12) == -1
    print('All tests passed')

if __name__ == '__main__':
    test()