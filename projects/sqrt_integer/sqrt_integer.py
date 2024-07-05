def floor_sqrt(X):
    if X < 0:
        raise ValueError("X must be non-negative")
    if X == 0 or X == 1:
        return X
    
    low, high = 1, X
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == X:
            return mid
        elif mid * mid < X:
            low = mid + 1
            result = mid
        else:
            high = mid - 1
    return result

def test():
    for i in range(100):
        assert floor_sqrt(i) == int(i ** 0.5)
    print("Passed all tests!")

if __name__ == '__main__':
    test()