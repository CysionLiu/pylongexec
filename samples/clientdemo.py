import socket

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
so.connect(("127.0.0.1", 6666))
while True:
    data = input('>')
    so.send(data.encode())
    if not data:
        break
    else:
        msg = so.recv(1024)
        print('from sever:', str(msg,'utf-8'))
so.close()
