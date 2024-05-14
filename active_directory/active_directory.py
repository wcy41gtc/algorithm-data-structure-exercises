class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    for g in group.get_groups():
        return is_user_in_group(user, g)
    return False

def test():
    # Test Case 1: Regular Input
    assert is_user_in_group(sub_child_user, parent) == True, "Test Case 1 Failed"
    print("Test Case 1 Passed")

    # Test Case 2: User not in group
    assert is_user_in_group("random_user", parent) == False, "Test Case 2 Failed"
    print("Test Case 2 Passed")

    # Test Case 3: Empty Group
    empty_group = Group("empty")
    assert is_user_in_group("random_user", empty_group) == False, "Test Case 3 Failed"
    print("Test Case 3 Passed")

    # Test Case 4: Empty User
    assert is_user_in_group("", parent) == False, "Test Case 4 Failed"
    print("Test Case 4 Passed")

if __name__ == "__main__":
    # Create a parent group
    parent = Group("parent")

    # Create a child group
    child = Group("child")

    # Create a sub-child group
    sub_child = Group("subchild")

    # Add the sub-child group to the child group
    child.add_group(sub_child)

    # Add the child group to the parent group
    parent.add_group(child)

    # Create a user
    sub_child_user = "sub_child_user"

    # Add the user to the sub-child group
    sub_child.add_user(sub_child_user)

    test()