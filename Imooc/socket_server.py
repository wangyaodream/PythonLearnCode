import socket
import random
# create instance

count = 0

sk = socket.socket()

# define ip address and port

ip_port = ("127.0.0.1",9999)
# bind listen
sk.bind(ip_port)

#最大连接数
sk.listen(5)
while True:

    print('waiting to accept.......')

    #接受数据
    conn,address = sk.accept()

    #define info

    msg = "sucessful connection"

    #return message
    conn.send(msg.encode())

    while True:
        #accept client info
        data = conn.recv(1024)
        print(data.decode())
        if data == b'exit':
            break
    #close
        conn.send(data)
        # send random num
        conn.send(str(random.randint(1,1000)).encode())
    count += 1
    if(count >= 3):
        break

    conn.close()

