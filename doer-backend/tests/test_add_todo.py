import json
from unittest.mock import MagicMock

import pytest

from src.functions.add_todo import handler
from src.shared.return_message import add_to_db_success, invalid_request_body


@pytest.fixture
def mock_table():
    return MagicMock()

def test_add_todo(mock_table):
    # simulates successfully add to database
    mock_table.put_item.return_value = {}
    mock_event = {
        'body': json.dumps({
            'id': '1',
            'title': 'test todo',
            'shared_with': None
        })
    }

    res = handler(event=mock_event, context=None, table=mock_table)
    assert res['statusCode'] == 201
    assert json.loads(res['body'])['message'] == json.loads(add_to_db_success()['body'])['message']

def test_add_todo_invalid_json_1(mock_table):
    # simulates missing title in request, should fail
    mock_table.put_item.return_value = {}
    mock_event = {
        'body': json.dumps({
            'id': '1',
            'title': ' ',
            'shared_with': None
        })
    }

    res = handler(event=mock_event, context=None, table=mock_table)
    assert res['statusCode'] == 400
    assert json.loads(res['body'])['error'] == json.loads(invalid_request_body()['body'])['error']

def test_add_todo_invalid_json_2(mock_table):
    # simulates missing title in request, should fail
    mock_table.put_item.return_value = {}
    mock_event = {
        'body': json.dumps({
            'id': '1',
            'shared_with': None
        })
    }

    res = handler(event=mock_event, context=None, table=mock_table)
    assert res['statusCode'] == 400
    assert json.loads(res['body'])['error'] == json.loads(invalid_request_body()['body'])['error']