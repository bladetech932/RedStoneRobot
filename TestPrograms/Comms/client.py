import socket

host = '47.217.97.185' #public ip determined py server
port = 932

message = ''

s = socket.socket()
s.connect(('127.0.0.1', port))


while message != 'q':
    message = input('--->')
    s.send(message.encode())
    if not message:
        break
    data = s.recv(1024).decode()

    print('Received from Server : ' + data)

s.close()
