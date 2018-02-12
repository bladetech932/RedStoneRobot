import pygame
# import time

pygame.init()
pygame.joystick.init()

joy_count = pygame.joystick.get_count()
print("num of joysticks", joy_count)
xbone = pygame.joystick.Joystick(0)
xbone.init()
print("name is", xbone.get_name())
print("num of axes", xbone.get_numaxes())
print("num of buttons", xbone.get_numbuttons())


def get_joystick_data(joystick):
    axes_data = []
    button_data = []
    hat_data = []
    joystick_data = [axes_data, button_data, hat_data]
    if pygame.event.get():
        for axis in range(joystick.get_numaxes()):
            mod_axis = (round(joystick.get_axis(axis)*127))
            if abs(mod_axis) < 15:
                mod_axis = 0
            joystick_data[0].append(mod_axis)
        for button in range(joystick.get_numbuttons()):
            joystick_data[1].append(joystick.get_button(button))
        for hat in range(joystick.get_numhats()):
            joystick_data[2].append(joystick.get_hat(hat))
    return joystick_data


xbone_data = get_joystick_data(xbone)
if xbone_data[0]:
    print("axes : ", xbone_data[0])
    print("buttons : ", xbone_data[1])
    print("hats : ", xbone_data[2])
