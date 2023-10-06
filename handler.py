import json

def do_something():
    # TODO implement
    return {
        'statusCode': 202,
        'body': json.dumps('Hello from Lambda!')
    }


print('Loading function')

def lambda_handler(event, context):
    '''Provide an event that contains the following keys:

      - operation: one of the operations in the operations dict below
      - payload: a JSON object containing parameters to pass to the
                 operation being performed
    '''

    # define the functions used to perform the CRUD operations
    def ddb_create(x):
        do_something()

    def ddb_read(x):
        do_something()

    def ddb_update(x):
        do_something()

    def ddb_delete(x):
        do_something()

    def echo(x):
        return x

    if 'operation' not in event:
        print('not in')
        return do_something()

    operation = event['operation']

    operations = {
        'create': ddb_create,
        'read': ddb_read,
        'update': ddb_update,
        'delete': ddb_delete,
        'echo': echo,
    }

    if operation in operations:
        return operations[operation](event.get('payload'))
    else:
        raise ValueError('Unrecognized operation "{}"'.format(operation))
