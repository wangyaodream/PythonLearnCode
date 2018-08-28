import socketserver #非阻塞
import random

#定义一个类
class MyServer(socketserver.BaseRequestHandler):
    #如果handle方法出现报错，会跳过，setup方法和finish方法无论如何都会执行
    def setup(self):
        pass

    def handle(self):
        conn = self.request
        msg = 'Hello world!'
        #send message
        conn.send(msg.encode())
        while True:
            data = conn.recv(1024)
            print(data.decode())

            if data ==  b'exit':
                break
            conn.send(data)
            conn.send(str(random.randint(1,1000)).encode())
        conn.close()
    def finish(self):
        pass


if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(('127.0.0.1',9999),MyServer)
    #开启异步多线程
    server.serve_forever()