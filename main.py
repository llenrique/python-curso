"""Platzi ventas."""
import sys

clients = 'enrique,miguel,'


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


def create_client(client_name):
    """Create client."""
    global clients
    if client_name not in clients:
        clients += client_name
        _add_coma()
    else:
        print('Client {} already exist in clien\'s list!'.format(client_name))


def read_clients_list():
    """List clients."""
    global clients
    print(clients)


def update_client(client_name):
    """Update client."""
    global clients
    if client_name in clients:
        updated_client_name = _get_client_name('new name')
        clients = clients.replace(client_name + ',', updated_client_name + ',')
        read_clients_list()
    else:
        print('Client not found!')


def delete_client(client_name):
    """Delete a client."""
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
        read_clients_list()
    else:
        print('Client not found!')


def search_client(client_name):
    """Search a client."""
    global clients
    clients = clients.split(',')
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


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


def _add_coma():
    global clients
    clients += ', '


if __name__ == '__main__':
    print_welcome()
    command = input()
    command = command.upper()

    if(command == 'C'):
        client_name = _get_client_name()
        create_client(client_name)
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
