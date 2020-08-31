import socket

address_to_server = ('localhost', 8686)

while True:
    client = socket.socket()
    client.connect(address_to_server)

    text = input('user2: ')

    client.send(text.encode())

    data = client.recv(1024)
    print('user1: ' + data.decode())

    client.close()
