def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = low + (high - low) // 2
        # print(f"mid: {mid}")
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)
    
def binary_search(arr, target):
    return binary_search_recursive(arr, target, 0, len(arr) - 1)

def test():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    assert binary_search(arr, target) == 4

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 1
    assert binary_search(arr, target) == 0

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 9
    assert binary_search(arr, target) == 8

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 10
    assert binary_search(arr, target) == -1

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 0
    assert binary_search(arr, target) == -1

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 6
    assert binary_search(arr, target) == 5

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 7
    assert binary_search(arr, target) == 6

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 8
    assert binary_search(arr, target) == 7

    print("All tests passed.")

if __name__ == "__main__":
    test()