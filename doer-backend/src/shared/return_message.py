import json


def success(message):
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': "completed successfully."
        })
    }

def add_to_db_success():
    return {
        'statusCode': 201,
        'body': json.dumps({
            'message': "Added successfully."
        })
    }

def invalid_request_body():
    return {
        'statusCode': 400,
        'body': json.dumps({
            'error': 'Invalid request body.'
        })
    }

def server_error():
    return {
        'statusCode': 500,
        'body': json.dumps({
            'error': 'Somthing went wrong, try again.'
        })
    }