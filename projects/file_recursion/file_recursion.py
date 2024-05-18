import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # Check if the path exists
    if not os.path.exists(path):
        return []
    else:
        # Check if the path is a file
        if os.path.isfile(path):
            # Check if the file has the suffix
            if path.endswith(suffix):
                return [path]
            else:
                return []
        # Check if the path is a directory
        elif os.path.isdir(path):
            # Initialize the list of paths
            paths = []
            # Iterate over the files and directories in the path
            for file in os.listdir(path):
                # Recursively call the function on the file
                paths += find_files(suffix, os.path.join(path, file))
            return paths
        else:
            return []

# Test cases
def test_function(test_case):
    output = find_files(test_case[0], test_case[1])
    if set(output) == set(test_case[2]):
        print("Pass")
    else:
        print("Fail")

def test():
    # Test case 1
    path = "./testdir"
    suffix = ".c"
    output = ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c']
    test_case = [suffix, path, output]
    test_function(test_case)

    # Test case 2
    path = "./testdir"
    suffix = ".h"
    output = ['./testdir/subdir1/a.h', './testdir/subdir3/subsubdir1/b.h', './testdir/t1.h', './testdir/subdir5/a.h']
    test_case = [suffix, path, output]
    test_function(test_case)

    # Test case 3
    path = "./testdir"
    suffix = ".z"
    output = []
    test_case = [suffix, path, output]
    test_function(test_case)

    # Test case 4 (Edge Case) - Empty directory
    path = "./emptydir"
    suffix = ".c"
    output = []
    test_case = [suffix, path, output]
    test_function(test_case)

    # Test case 5 (Edge Case) - Non existent directory
    path = "./nonexistentdir"
    suffix = ".c"
    output = []
    test_case = [suffix, path, output]
    test_function(test_case)

    # Test case 6 (Edge Case) - Invalid suffix
    path = "./testdir"
    suffix = ".exe"
    output = []
    test_case = [suffix, path, output]
    test_function(test_case)

    # Test case 7 (Edge Case) - single file in root directory
    path = "./singlefile"
    suffix = ".txt"
    output = ['./singlefile/singlefile.txt']
    test_case = [suffix, path, output]
    test_function(test_case)

    # Test case 8 (deeply nested directories)
    path = "./deepdir"
    suffix = ".c"
    output = ['./deepdir/subdir1/subdir2/subdir3/subdir4/subdir5/a.c']
    test_case = [suffix, path, output]
    test_function(test_case)

if __name__ == "__main__":
    test()

