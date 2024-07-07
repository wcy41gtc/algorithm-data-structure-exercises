def merge_sort_desc(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort_desc(left_half)
        merge_sort_desc(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def rearrange_max_sum(arr):
    merge_sort_desc(arr)  # Sort the array in descending order

    num1, num2 = [], []

    for i, digit in enumerate(arr):
        if i % 2 == 0:
            num1.append(str(digit))
        else:
            num2.append(str(digit))

    # Convert lists to integers
    num1 = int("".join(num1))
    num2 = int("".join(num2))

    return [num1, num2]

def test():
    assert rearrange_max_sum([1, 2, 3, 4, 5]) == [531, 42]
    assert rearrange_max_sum([4, 6, 2, 5, 9, 8]) == [964, 852]
    assert rearrange_max_sum([1, 2, 3, 4, 5, 6]) == [642, 531]
    assert rearrange_max_sum([1, 2, 3, 4, 5, 6, 7]) == [7531, 642]
    print('All tests passed')

if __name__ == '__main__':
    test()