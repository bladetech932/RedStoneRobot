import socket, sys, shutil, pickle

test_dict = {"test":"this","is":"a"}
print(sys.getsizeof(test_dict))
pickled_dict = pickle.dumps(test_dict)

host = '47.217.97.185' #public ip determined py server
port = 932
s = socket.socket()
s.connect(('127.0.0.1', port))

while True:
    print(sys.getsizeof(pickled_dict))
    s.send(pickled_dict)
    data = str(s.recv(1024))

    print('Received from Server : ' + data)
    break
s.close()
