import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
trig = 23
echo = 24

print("distance measurement in progress")

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)


count = 0
total = 0
avg = 0

GPIO.output(trig,False)
print("Settle")
time.sleep(2)
while True:
        #count += 1
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

GPIO.cleanup()
