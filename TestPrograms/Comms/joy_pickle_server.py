import pickle, socket, sys, shutil

host = "127.0.0.1" #private address locked for host
port = 932
s = socket.socket()
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port)) #bind port
s.listen(1) #requests to hold
while True:
    print("waiting for connection..")
    conn, addr = s.accept()
    print('connection from: ' + str(addr))
    while True:
        data = conn.recv(1024)
        if not data:
            print("connection closed")
            exit()
        unpickled_dict = pickle.loads(data)
        print(unpickled_dict)
        #print ('sending: ' + str(data))
        conn.send(data)
        break
    break
conn.close
s.close()
