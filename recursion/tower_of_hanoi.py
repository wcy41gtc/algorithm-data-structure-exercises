# Problem Statement
# The Tower of Hanoi is a puzzle where we have three rods and n unique sized disks.
# Initally, all the n disks are present on the source rod. The final objective of the 
# puzzle is to move all disks from the source rod to the destination rod using the auxiliary rod.
# However, there are some rules applicable to all rods:
# 1. Only one disk can be moved at a time.
# 2. A disk can be moved only if it is on the top of a rod.
# 3. No disk can be placed on the top of a smaller disk.
    
# You will be given the number of disks num_disks as the input parameter. 
# Write a recursive function tower_of_Hanoi() that prints the "move" steps in order to move 
# num_disks number of disks from Source to Destination using the help of Auxiliary rod.

# Recursive Solution
def tower_of_Hanoi_soln(num_disks, source, auxiliary, destination):
    
    # Base condition
    if num_disks == 0:
        return

    # Termination condition
    if num_disks == 1:
        print("{} {}".format(source, destination))
        return
    

    '''Just think of one iteration, rest the Recursion will take care!'''
    
    # Step 1: Move `num_disks - 1` from source to auxiliary
    tower_of_Hanoi_soln(num_disks - 1, source, destination, auxiliary)
    
    # Step 2: Now you are left with the only largest disk at source. 
    # Move the only leftover disk from source to destination
    print("{} {}".format(source, destination))
    
    # Step 3: Move `num_disks - 1` from auxiliary to destination
    tower_of_Hanoi_soln(num_disks - 1, auxiliary, source, destination)
    
def tower_of_Hanoi(num_disks):
    tower_of_Hanoi_soln(num_disks, 'S', 'A', 'D')

def main():
    num_disks = 3
    tower_of_Hanoi(num_disks)

if __name__ == '__main__':
    main()