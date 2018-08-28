import socket

ip_port = ('127.0.0.1',9999)

sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    msg_input = input('please input your code:')

    if msg_input == 'exit':
        break
    #UDP 的数据发送
    sk.sendto(msg_input.encode(),ip_port)
sk.close()