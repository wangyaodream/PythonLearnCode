import socket

#create instance

client = socket.socket()

ip_port = ('127.0.0.1',9999)

# connect server
client.connect(ip_port)

#send info
while True:

    # accept info from server
    data = client.recv(1024)

    # print data

    print(data.decode())  # 对返回结果进行解码 (返回的是byte类型)
    #input message
    msg_input = input('Please enter your code:')
    #msg send
    client.send(msg_input.encode())
    if msg_input == "exit":
        break
    data = client.recv(1024)
    print(data.decode())