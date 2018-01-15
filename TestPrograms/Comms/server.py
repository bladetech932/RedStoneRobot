import socket
host = '10.0.0.50' #private address locked for host
port = 932

s = socket.socket()
s.bind(('127.0.0.1',port)) #bind port
s.listen(5) #requests to hold
while True:
    print("waiting for connection..")
    conn, addr = s.accept()
    print('connection from: ' + str(addr))
    while True:
        data = conn.recv(1)#.decode()
        print(type(data))
        if not data:
            print("connection closed")
            break
        print(data)
        #print ('sending: ' + str(data))
        #conn.send(data.encode())
    break
conn.close
s.close()
