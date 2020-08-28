import socket

my_name = 'user2'.encode()

sock = socket.socket()

sock_user = socket.socket()
sock_user.connect(('localhost', 9090))

print('connected')

sock_user.send(my_name)

sock.bind(('', 9091))
sock.listen(1)

conn_global, adr_global = sock.accept()
user_name = conn_global.recv(1024)

conn_global.close()

print(user_name.decode())

while True:
    text = input().encode()
    sock.send(text)

    conn, adr = sock.accept()

    while True:
        data = conn.recv(1024)
        if not data:
            break
        data = data.decode()
        print(user_name + ': ' + data)

    conn.close()
