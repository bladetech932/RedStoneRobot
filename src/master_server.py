
#!/usr/bin/env python

import pickle
import socket
import Adafruit_PCA9685 as pca
import numpy as np
import cv2
import os
import RPi.GPIO as GPIO
import time



cap = cv2.VideoCapture(0)
pwm = pca.PCA9685()
pwm.set_pwm_freq(60)

# Sets up what pins on the PCA that is being used, change for which pins you are using.

FL_channel = 0
FR_channel = 1
BL_channel = 2
BR_channel = 3


port = 55555
#Creating a socket that is called s
s = socket.socket()
s.bind(('', port))
s.listen(1)
print("waiting for connection...")
conn, addr = s.accept()

def pic():
    # This makes the system take a picture and call it test.jpg
    s.system("raspistill -t 1000 -vf -n -hf -o test.jpg -w 640 -h 480 -q 50")
    #This sets the variable img to test.jpg so that it can be edited.
    img = cv2.imread('test.jpg', 0)

def picShow():
    #Shows the picture saved in img for testing purposes.
    cv2.imshow('video', img)

def circles():
    # This method draws the circles on the image and gets the distance from the center of the pic to the center of the circle
    # Note this needs to be edited to return those values.
    # Note add more exceptions.
    img = cv2.imread('test.jpg', 0)
    img_height, img_width = img.shape
    img = cv2.medianBlur(img, 5)
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=40, minRadius=10, maxRadius=50)
    apple = 0
    lamp = 0
    circles = np.uint16(np.around(circles))

    #Finding them circles
    for i in circles[0, :]:
        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)

        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

        cv2.circle(cimg, (int(img_width/2), int(img_height/2)), 2, (255, 0, 0), 3)

        apple = i[0]
        lamp = i[1]

        cv2.arrowedLine(cimg, (int(img_width/2), int(img_height/2)), (apple, lamp), (0, 89, 217), 2)
        list = [apple, lamp]
    return list


def manualDrive():
    #This method is to allow the manuel controll of the robot using a XBOX ONE controller.
    #This should be put into a loop, so that it can be run repeatedly.
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

def ping(int pinNum):

    GPIO.setmode(GPIO.BCM)
    trig = 23
    echo = 24

    #print("distance measurement in progress")

    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)

    count = 0
    total = 0
    avg = 0

    GPIO.output(trig,False)
    #print("Settle")
    time.sleep(2)
  
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    while GPIO.input(echo)==0:
        #print("time is ",time.time())
        pulse_start = time.time()
    while GPIO.input(echo)==1:
        #print("time is ",time.time())
         pulse_end = time.time()
         pulse_length = pulse_end - pulse_start

    dist = 17150 * pulse_length
    #total += dist
    #avg = total / count
    #if count %10 == 0:
     if dist <= 10000:
        print("distance:",round(dist),"cm")
      #count = 0
      #total = 0
      time.sleep(.02)
    return distance
    GPIO.cleanup()

def pings():
    table = []
    #This should function like ping, but should return an array of 8 legth
    for i in range(8):
        table[i] = ping(i)
    return table    
def laser():

    sensor = 7
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    current = GPIO.input(sensor)
    previous = current
    def printState(current):
        print 'GPIO pin %s is %s' % (sensor, 'HIGH' if current else 'LOW')
    printState(current)
    while True:
        current = GPIO.input(sensor)
        if current != previous:
            printState(current)
        previous = current
        time.sleep(0.1)
    GPIO.cleanup()

def rightMove():
#Make John do this
def leftMove():
#Make John do this
def forwardMove():
#Make John do this
def backwardMove():
#Make John do this
def rightStrafe():
#Make John do this
def leftStrafe():
#Make John do this
def navigation():
    sensor = []
    sensor = ping()
    if (sensor[0] >= 1 and sensor[1] >= 1 and sensor[2] >= 1 and sensor[3] >= 1 and sensor[4] >= 1 and sensor[5] >= 1 and sensor[6] >= 1 and sensor[7] >= 1):
        forwardMove()
    else if (sensor[0] <= 1 and sensor[1] >= 1 and sensor[2] >= 1 and sensor[3] >= 1 and sensor[4] >= 1 and sensor[5] >= 1 and sensor[6] >= 1 and sensor[7] >= 1):
        rightStrafe()
    else if sensor[0] >= 1 and sensor[1] >= 1 and sensor[2] >= 1 and sensor[3] >= 1 and sensor[4] >= 1 and sensor[5] >= 1 and sensor[6] >= 1 and sensor[7] >= 1):
        leftStrafe()
    else if sensor[0] >= 1 and sensor[1] >= 1 and sensor[2] >= 1 and sensor[3] >= 1 and sensor[4] >= 1 and sensor[5] >= 1 and sensor[6] >= 1 and sensor[7] >= 1):
        rightMove()
    else if sensor[0] >= 1 and sensor[1] >= 1 and sensor[2] >= 1 and sensor[3] >= 1 and sensor[4] >= 1 and sensor[5] >= 1 and sensor[6] >= 1 and sensor[7] >= 1):
        leftMove()
    else if sensor[0] >= 1 and sensor[1] >= 1 and sensor[2] >= 1 and sensor[3] >= 1 and sensor[4] >= 1 and sensor[5] >= 1 and sensor[6] >= 1 and sensor[7] >= 1):
        backwardMove()
#Beginning and pick up
def beggining():
    sensors = []
    sensor = ping()
    # Not to zone yet
    if():
        navigation()
    #Inside the zone
    else if():
        forwardMove()
        pic()
        distance = []
        distance = circles()
        # Not on target
        if (distance):
# After pick up to bridge
def middle():
    #Find a way to check to see how many turns the robot has done to know when the bridge is coming up.
    right = 0;
    while(right < 5):
        navigation();
    navigation()

def bridge():


def findingZone():
    distance = []

    navigation()
    forwardMove()
    pic()


    try:
        distance = circles()
    except Exception as e:
        navigation()


def zone():

def slolom():
    while(true)
    distance = []
    distance = ping()
    if(distance[0] >= 1 and distance[1] <= 1 and distance[2] <= 1 and distance[4] >= 1):
        leftStrafe()
    else if(distance[0] <=1 and distance[1] >= 1 and distance [2] >= 1 and distance[4] <= 1)
        forwardMove()
    else if(distance[0] <= 1 and distance[1] <= 1 and distance[2] <= 1 and distance[3] >=1 and distance[4] >= 1 and distance[7] >= 1)
        rightStrafe()
    else if()    

def afterslolomToSprint():

def sprint():
    lol = []
    lol = pings()
    if():
      forwardMove()
    else if():
        rightStrafe()
    else if():
         leftStrafe()
            
conn.close()
s.close()
