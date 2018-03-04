#!/usr/bin/env python

import pickle
import socket
import Adafruit_PCA9685 as pca
import numpy as np
import cv2
import os





def pic():
    os.system("raspistill -t 1000 -vf -n -hf -o test.jpg -w 640 -h 480 -q 50")
    img = cv2.imread('test.jpg', 0)
    cv2.imshow('video', img)

def loop():
    while True:

        pickled_data = conn.recv(1024)
        if not pickled_data:
            break
        try:
            data = pickle.loads(pickled_data)
            FL_motor = ((-data[0][1] + data[0][0]) * -2 + 420)
            FR_motor = ((-data[0][1] - data[0][0]) * 2 + 420)
            BL_motor = ((-data[0][1] - data[0][0]) * -2 + 420)
            BR_motor = ((-data[0][1] + data[0][0]) * 2 + 420)
            print("FL:", FL_motor, " FR:", FR_motor, " BL:", BL_motor, " BR:", BR_motor)

            pwm.set_pwm(FL_channel, 0, FL_motor)
            pwm.set_pwm(FR_channel, 0, FR_motor)
            pwm.set_pwm(BL_channel, 0, BL_motor)
            pwm.set_pwm(BR_channel, 0, BR_motor)

            pass
        except Exception as e:
            print("Damn errors")
            raise

        if data[1][0] is 1:
            break






pwm = pca.PCA9685()
pwm.set_pwm_freq(60)
FL_channel = 0
FR_channel = 1
BL_channel = 2
BR_channel = 3

port = 55555
s = socket.socket()
s.bind(('', port))
s.listen(1)
print("waiting for connection...")
conn, addr = s.accept()
# print("connected to: ", addr)
while True:
    loop()
    pic()

conn.close()
s.close()
