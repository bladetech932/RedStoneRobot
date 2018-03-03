#!/usr/bin/python3

import _thread
import threading as trd
import time

# Define a function for the thread


def print_time(delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % ("name", time.ctime(time.time())))


# Create two threads as follows
try:
    _thread.start_new_thread(print_time, (2, ))
    _thread.start_new_thread(print_time, (4, ))
    print(trd.activeCount())
    print(trd.enumerate())
except:
    print("Error: unable to start thread")

while 1:
    pass
