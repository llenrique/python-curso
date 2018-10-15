"""Platzi ventas."""


clients = 'enrique, miguel, '


def create_client(client_name):
    """Create client."""
    global clients
    if client_name not in clients:
        clients += client_name
        _add_coma()
    else:
        print('Client already exist in clien\'s list!')


def _add_coma():
    global clients
    clients += ', '


def list_clients():
    """List clients."""
    global clients
    print(clients)


def print_welcome():
    """Give a wellcome."""
    print('WELCOME TO Platzi ventas!')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C] Create client')
    print('[U] Update client')
    print('[D] Delete client')


def update_client(client_name):
    """Update client."""
    global clients
    if client_name in clients:
        updated_client_name = _get_client_name('new name')
        clients = clients.replace(client_name + ',', updated_client_name + ',')
        list_clients()
    else:
        print('Client not found!')


def _get_client_name(type_to_manage='name'):
    """Get the client name."""
    return input('What is the client {}: '.format(type_to_manage))


if __name__ == '__main__':
    print_welcome()
    command = input()
    command = command.upper()

    if(command == 'C'):
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    elif command == 'U':
        client_name = _get_client_name()
        update_client(client_name)
    else:
        print('Invalid command')
