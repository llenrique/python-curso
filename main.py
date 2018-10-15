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
    print('[D] Delete client')


if __name__ == '__main__':
    print_welcome()
    command = input()

    if(command == 'C'):
        client_name = input('What is the client name? ')
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    else:
        print('Invalid command')
