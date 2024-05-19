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
    # Input validation
    if not isinstance(user, str):
        raise ValueError("User must be a string.")
    if not isinstance(group, Group):
        raise ValueError("Group must be an instance of the Group class.")
    if user == "":
        return False
    if user in group.get_users():
        return True
    for g in group.get_groups():
        if is_user_in_group(user, g):
            return True
    return False

if __name__ == "__main__":
    # Define groups
    parent = Group("parent")
    child1 = Group("child1")
    child2 = Group("child2")
    sub_child1 = Group("subchild1")
    sub_child2 = Group("subchild2")

    # Add users to groups
    parent.add_user("parent_user")
    child1.add_user("child1_user")
    child2.add_user("child2_user")
    sub_child1.add_user("subchild1_user")
    sub_child2.add_user("subchild2_user")

    # Define group hierarchy
    parent.add_group(child1)
    parent.add_group(child2)
    child1.add_group(sub_child1)
    child2.add_group(sub_child2)

    # Test is_user_in_group function
    assert is_user_in_group("parent_user", parent) == True
    assert is_user_in_group("child1_user", parent) == True
    assert is_user_in_group("child2_user", parent) == True
    assert is_user_in_group("subchild1_user", parent) == True
    assert is_user_in_group("subchild2_user", parent) == True
    assert is_user_in_group("subchild2_user", child1) == False
    assert is_user_in_group("non_existent_user", parent) == False
    # Test input validation
    # Test with non-string user
    try:
        is_user_in_group(123, parent)
    except ValueError as e:
        assert str(e) == "User must be a string.", "Test case failed: Expected ValueError for non-string user"
    
    # Test with non-Group instance as group
    try:
        is_user_in_group("parent_user", "not_a_group")
    except ValueError as e:
        assert str(e) == "Group must be an instance of the Group class.", "Test case failed: Expected ValueError for non-Group instance"
    
    # Test with empty user string
    assert is_user_in_group("", parent) == False, "Test case failed: Empty user string should not be found in any group"
    
    # Test with None user
    try:
        is_user_in_group(None, parent)
    except ValueError as e:
        assert str(e) == "User must be a string.", "Test case failed: Expected ValueError for None user"
    
    print("All test cases passed!")