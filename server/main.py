import socket

my_name = 'user1'.encode()

sock = socket.socket()

sock.bind(('', 9090))
sock.listen(1)

print('connected')

conn_global, adr_global = sock.accept()

user_name = conn_global.recv(1024)

conn_global.close()

print(user_name.decode())

sock_user = socket.socket()
sock_user.connect(('localhost', 9091))

sock_user.send(my_name)

while True:
    conn, adr = sock.accept()

    while True:
        data = conn.recv(1024)
        if not data:
            break
        data = data.decode()
        print(user_name + ': ' + data)

    conn.close()

    text = input().encode()
    sock.send(text)
