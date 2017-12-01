import socket

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
so.bind(('127.0.0.1', 6666))
so.listen(5)
print('等待客户端连接')
while True:
    client_socket, address = so.accept()
    print(client_socket.getsockname(), '已连接')
    while True:
        msg = client_socket.recv(1024)
        if not msg:
            break
        else:
            print('receive from client:',str(msg,'utf-8'))
            client_socket.send(msg)
    client_socket.close()
