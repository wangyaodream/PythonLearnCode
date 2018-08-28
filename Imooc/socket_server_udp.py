import socket

sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #IPv4 UDP通信方式

ip_port = ("127.0.0.1",9999)

sk.bind(ip_port)

while True:
    data = sk.recv(1024)

    print(data.decode())


