def staircase(n):
    num_dict = dict({})
    return staircase_faster(n, num_dict)

def staircase_faster(n, num_dict):
    if n == 1:
        output = 1
    elif n == 2:
        output = 2
    elif n == 3:
        output = 4
    else:
        if (n - 1) in num_dict:
            first_output = num_dict[n - 1]
        else:
            first_output =  staircase_faster(n - 1, num_dict)
        
        if (n - 2) in num_dict:
            second_output = num_dict[n - 2]
        else:
            second_output = staircase_faster(n - 2, num_dict)
            
        if (n - 3) in num_dict:
            third_output = num_dict[n - 3]
        else:
            third_output = staircase_faster(n - 3, num_dict)
        
        output = first_output + second_output + third_output
    
    num_dict[n] = output
    return output

def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = staircase(n)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

def test():
    n = 3
    solution = 4
    test_case = [n, solution]
    test_function(test_case)

    n = 4
    solution = 7
    test_case = [n, solution]
    test_function(test_case)

    n = 7
    solution = 44
    test_case = [n, solution]
    test_function(test_case)

    n = 20
    solution = 121415
    test_case = [n, solution]
    test_function(test_case)

if __name__ == '__main__':
    test()