def contains(target, source):
    # naive implementation of binary search algorithm
    if len(source) == 0:
        return False
    center = (len(source) - 1) // 2
    if source[center] == target:
        return True
    elif source[center] < target:
        return contains(target, source[center + 1:])
    else:
        return contains(target, source[:center])
    
def test():
    assert contains(1, [1, 2, 3, 4, 5]) == True
    assert contains(5, [1, 2, 3, 4, 5]) == True
    assert contains(3, [1, 2, 3, 4, 5]) == True
    assert contains(6, [1, 2, 3, 4, 5]) == False
    assert contains(0, [1, 2, 3, 4, 5]) == False
    print('All tests passed')

if __name__ == '__main__':
    test()