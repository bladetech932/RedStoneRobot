import pygame
import pickle
import socket
# import sys
import time


host = '10.0.0.50'  # private address for testing
# host = '47.217.107.128'  # public address for runtime
port = 55555

s = socket.socket()

pygame.init()
pygame.joystick.init()

xbone = pygame.joystick.Joystick(0)
xbone.init()

joystick_dead_band = 0  # max value = 127

# print("num of joysticks", pygame.joystick.get_count())
# print("name is", xbone.get_name())
# print("num of axes", xbone.get_numaxes())
# print("num of buttons", xbone.get_numbuttons())


def get_joystick_data(joystick):
    axes_data = []
    button_data = []
    hat_data = []
    joystick_data = [axes_data, button_data, hat_data]
    for event in pygame.event.get():
        pass
    for axis in range(joystick.get_numaxes()):
        mod_axis = (round(joystick.get_axis(axis)*127))
        if abs(mod_axis) < joystick_dead_band:
            mod_axis = 0
        joystick_data[0].append(mod_axis)
    for button in range(joystick.get_numbuttons()):
        joystick_data[1].append(joystick.get_button(button))
    for hat in range(joystick.get_numhats()):
        joystick_data[2].append(joystick.get_hat(hat))
    return joystick_data


s.connect((host, port))
while xbone.get_button(7) is 0:
    xbone_data = get_joystick_data(xbone)
    print(xbone_data)
    pickled_xbone = pickle.dumps(xbone_data)
    # print(sys.getsizeof(pickled_xbone))
    s.send(pickled_xbone)
    time.sleep(0.1)
