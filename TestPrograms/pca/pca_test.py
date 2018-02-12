#!/usr/bin/env python

import Adafruit_PCA9685 as pca
# import time

pwm = pca.PCA9685()
pwm.set_pwm_freq(60)

for i in range(0, 15):
    pwm.set_pwm(i, 0, 425)  # values from 0 to 4096 #12 bit resolution
