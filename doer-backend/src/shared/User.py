import uuid


class User:
    def __init__(self, user_id: uuid, username: str):
        self.user_id = user_id
        self.username = username

    def __str__(self):
        return self.username
