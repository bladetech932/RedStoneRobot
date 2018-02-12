import pickle
import socket

port = 55555
s = socket.socket()
s.bind(('127.0.0.1', port))
s.listen(1)
print("waiting for connection...")
conn, addr = s.accept()
# print("connected to: ", addr)
while True:
    pickled_data = conn.recv(1024)
    if not pickled_data:
        break
    try:
        data = pickle.loads(pickled_data)
    except Exception as e:
        print("fail")
    print(data)
conn.close()
s.close()
