import json
import uuid
from datetime import datetime

from src.shared.User import User


class Todo:
    def __init__(self, todo_id: uuid, title: str, date_added: datetime, date_completed: datetime|None, author: User, shared_with: User):
        self.todo_id = todo_id
        self.title = title
        self.date_added = date_added
        self.date_completed = date_completed
        self.author = author
        self.shared_with = shared_with

    def is_completed(self):
        return self.date_completed is not None

    def database_format(self):
        return {
            'pk': f'USER#{self.author.user_id}',
            'sk': f'TODO#{self.date_added}#{self.todo_id}',
            'title': self.title,
            'completed_on': self.date_completed,
            'author': self.author.username,
            'shared_with': self.shared_with.user_id
        }

    @staticmethod
    def json_format(sk: str, title: str, completed_on: datetime|None, author: str, shared_with: str):
        sk_arr = sk.split('#')
        return json.dumps({
            'id': sk_arr[1] + sk_arr[2],
            'title': title,
            'completed_on': completed_on,
            'author': author,
            'shared_with': shared_with
        })