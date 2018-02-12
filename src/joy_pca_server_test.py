#!/usr/bin/env python

import pickle
import socket
import Adafruit_PCA9685 as pca

pwm = pca.PCA9685()
pwm.set_pwm_freq(60)
pwm_channel = 0

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
    y_axis = (data[0][1] * -2 + 400)
    pwm.set_pwm(pwm_channel, 0, y_axis)
conn.close()
s.close()
