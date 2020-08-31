import socket

_server_address = ('localhost', 8686)

server_socket = socket.socket()
server_socket.bind(_server_address)
server_socket.listen(1)
print('server is running, please, press ctrl+c to stop')



while True:
    connection, address = server_socket.accept()
    data = connection.recv(1024)
    print('user2: ' + data.decode())

    text = input('user1: ')

    connection.send(text.encode())

    connection.close()
