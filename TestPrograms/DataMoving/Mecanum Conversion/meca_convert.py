# import math
import pygame
import sys


def meca_convert(x, y):
    print(x, y)


pygame.init()
pygame.joystick.init()
controllers = pygame.joystick.get_count()
if controllers < 1:
    print("no controller")
    sys.exit(0)

xbone = pygame.joystick.Joystick(0)
xbone.init()

while True:
    for event in pygame.event.get():
        pass
    print(xbone.get_button(7))
    if xbone.get_button(7) is 0:
        x_input = xbone.get_axis(0)
        y_input = xbone.get_axis(1)
        # print(x_input, y_input)
