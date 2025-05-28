import json
import os
import uuid
from datetime import datetime
import boto3
from botocore.exceptions import ClientError

from src.shared.Todo import Todo
from src.shared.User import User
from src.shared.return_message import invalid_request_body, server_error, add_to_db_success
from src.shared.validate_parameters import is_valid


def get_table():
    dynamodb = boto3.resource('dynamodb')
    return dynamodb.Table(os.environ['TABLE_NAME'])

def find_user_by_id(user_id, table=None) -> User|None:
    if table is not None:
        # replace with actual db call
        if user_id == '1':
            return User(1, "test user")

    return None

def handler(event, context, table=None):
    if table is None:
        # to allow this function to be tested locally with stub table
        table = get_table()

    try:
        # extract data from event
        body = json.loads(event['body'])
        user_id = body['id']
        author = find_user_by_id(user_id, table)
        title = body['title']
        shared_with = find_user_by_id(body['shared_with'] or "", table)

        # validate data
        if not is_valid(user_id.strip(), title.strip(), author.username):
            return invalid_request_body()

        # send to db
        table.put_item(Item=Todo(
            todo_id=uuid.uuid1(),
            title=title,
            date_added=datetime.now(),
            date_completed=None,
            author=author,
            shared_with=shared_with or None
        ).database_format())
        return add_to_db_success()

    except (json.JSONDecodeError, KeyError):
        # if json received is missing one or more params
        return invalid_request_body()
    except ClientError as e:
        # is a server side error occurs
        print(e)
        return server_error()