"""Platzi ventas."""
import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software engenieer'
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data engenieer'
    }
]


def print_welcome():
    """Give a wellcome."""
    print('WELCOME TO Platzi ventas!')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C] Create client')
    print('[R] Read client list')
    print('[U] Update client')
    print('[D] Delete client')
    print('[S] Search client')


def create_client(client):
    """Create client."""
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client {} already exist in clien\'s list!'.format(client_name))


def read_clients_list():
    """List clients."""
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']
        ))


def update_client(client_name):
    """Update client."""
    global clients

    if client_name in clients:
        updated_client_name = _get_client_name('new name')
        index = clients.index(client_name)
        clients[index] = updated_client_name
        read_clients_list()
    else:
        print('Client not found!')


def delete_client(client_name):
    """Delete a client."""
    global clients

    if client_name in clients:
        clients.remove(client_name)
        read_clients_list()
    else:
        print('Client not found!')


def search_client(client_name):
    """Search a client."""
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def _get_client_field(field_name):
    """Set client data."""
    field = None

    while not field:
        field = input('What is the client {}?'.format(field_name))

    return field


def _get_client_name(type_to_manage='name'):
    """Get the client name."""
    client_name = None

    while not client_name:
        client_name = input('What is the client {}: '.format(type_to_manage))

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


if __name__ == '__main__':
    print_welcome()
    command = input()
    command = command.upper()

    if(command == 'C'):
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(client)
        read_clients_list()

    elif command == 'R':
        read_clients_list()

    elif command == 'U':
        client_name = _get_client_name()
        update_client(client_name)

    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)

    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print('Client: {} not found'.format(client_name))

    else:
        print('Invalid command')
