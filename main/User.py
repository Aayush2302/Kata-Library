# class User : username,role
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def __repr__(self):
        return f"username: {self.username}, role: {self.role}"
