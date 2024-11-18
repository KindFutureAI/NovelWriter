import uuid
from .role import Role

class RoleManager:

    def __init__(self):
        self.roles = {}
    
    def create_role(self, name, description=None, tasks=[]):
        """ Create a new role """
        role_id = str(uuid.uuid4())
        role = Role(role_id, name, description,tasks)
        self.roles[role.name] = role

    def get_role(self, name):
        """ Get a role by name """
        return self.roles.get(name)

    def list_roles(self):
        """ List all roles """
        return list(self.roles.values())

