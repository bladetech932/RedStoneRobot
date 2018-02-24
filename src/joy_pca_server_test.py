#!/usr/bin/env python

import pickle
import socket
import Adafruit_PCA9685 as pca

pwm = pca.PCA9685()
pwm.set_pwm_freq(60)
FL_channel = 0

port = 55555
s = socket.socket()
s.bind(('', port))
s.listen(1)
print("waiting for connection...")
conn, addr = s.accept()
# print("connected to: ", addr)
while True:
    pickled_data = conn.recv(1024)
    if not pickled_data:
        break
    data = pickle.loads(pickled_data)
    FL_motor = (data[0][1] * -2 + 400)
    pwm.set_pwm(FL_channel, 0, FL_motor)
conn.close()
s.close()
