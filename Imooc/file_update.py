import socket

sk = socket.socket()

ip_port = ('127.0.0.1',9999)

sk.connect(ip_port)

#file upload
with open('socket_server_tcp2.py','rb') as f:
    for i in f:
        sk.send(i)

sk.send('quit'.encode())