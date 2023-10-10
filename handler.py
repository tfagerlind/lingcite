"""This file implements the AWS Lambda entry of LingCite."""
import json


def do_something():
    """Provide bogus Lambda Result JSON."""
    # TODO implement
    return {
        'statusCode': 202,
        'body': json.dumps('Hello from Lambda!')
    }


def lambda_handler(event, context):
    """Handle lambda event.

    This is the main Lambda entry of LingCite.

    Under construction. Currently it doesn't do anything interesting.
    """

    def do_something_with_payload(payload):
        """Do someting with payload."""
        return do_something()

    def echo(payload):
        """Echo payload."""
        return payload

    if 'operation' not in event:
        print('not in')
        return do_something()

    operation = event['operation']

    # supported operations
    operations = {
        'create': do_something_with_payload,
        'read': do_something_with_payload,
        'update': do_something_with_payload,
        'delete': do_something_with_payload,
        'echo': echo,
    }

    if operation in operations:
        return operations[operation](event.get('payload'))
    else:
        raise ValueError('Unrecognized operation "{}"'.format(operation))
