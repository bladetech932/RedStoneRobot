
#!/usr/bin/env python

import pickle
import socket
import Adafruit_PCA9685 as pca
import numpy as np
import cv2
import os

cap = cv2.VideoCapture(0)

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

'''
os.system("raspistill -t 1000 -vf -n -hf -o test.jpg -w 640 -h 480 -q 50")
img = cv2.imread('test.jpg', 0)
cv2.imshow('video', img)
'''


def pic():
    # Capture frame-by-frame
    ret, frame = cap.read()

    print("Im in the video loop")
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)


def loop():
    try:
        pickled_data = conn.recv(1024)
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
    except Exception as e:
        print(e)
while True:
    loop()
    pic()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



conn.close()
s.close()
=======
#!/usr/bin/env python

import pickle
import socket
import Adafruit_PCA9685 as pca
import numpy as np
import cv2
import os

cap = cv2.VideoCapture(0)

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

'''
os.system("raspistill -t 1000 -vf -n -hf -o test.jpg -w 640 -h 480 -q 50")
img = cv2.imread('test.jpg', 0)
cv2.imshow('video', img)
'''

-a
def pic():
    # Capture frame-by-frame
    ret, frame = cap.read()

    print("Im in the video loop")
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)


def loop():
    try:
        pickled_data = conn.recv(1024)
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
    except Exception as e:
        print(e)
while True:
    loop()
    pic()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



conn.close()
s.close()
>>>>>>> before discard
