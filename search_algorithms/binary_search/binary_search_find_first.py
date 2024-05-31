def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)
    
def find_first(target, source):
    index = recursive_binary_search(target, source)
    if index is None:
        return None
    while source[index] == target:
        if index == 0:
            return 0
        if source[index-1] == target:
            index -= 1
        else:
            return index
    return index

def test():
    assert find_first(1, [1, 2, 3, 4, 5]) == 0
    assert find_first(1, [2, 3, 4, 5]) == None
    assert find_first(1, [1, 1, 1, 1, 1]) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test()