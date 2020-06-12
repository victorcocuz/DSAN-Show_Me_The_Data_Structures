# Define group class
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

# Define method that checks if user is in a group
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # for group in group.get_groups:
    #     if user in group:
    if user in group.get_users():
        return True
    for group in group.get_groups():
        if is_user_in_group(user, group):
            return True
            
    return False

# Assign groups and users
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child_user = "child_user"
child.add_user(child_user)

child.add_group(sub_child)
parent.add_group(child)

# Test if users belong to groups
print(is_user_in_group(sub_child_user, sub_child)) # True
print(is_user_in_group(sub_child_user, parent)) # True
print(is_user_in_group(child_user, child)) # True
print(is_user_in_group(child_user, sub_child)) # False

