import pygame, socket, shutil, sys, pickle

print(sys.version_info[0],sys.version_info[1])

host = '127.0.0.1'
port = 932

s = socket.socket()
s.connect((host,port))

pygame.init()
pygame.joystick.init()
joy_count = pygame.joystick.get_count() #num of controllers connected
if joy_count==0: #controller check
    print("no controllers connected")
    exit()
#controller found
xbox = pygame.joystick.Joystick(0)
xbox.init()
data = []

while True:
    for event in pygame.event.get():
        for axis in range(xbox.get_numaxes()):
            data.append(round(xbox.get_axis(axis)*-127)+127)
        for button in range(xbox.get_numbuttons()):
            data.append(xbox.get_button(button))
        #print(data_list)
        pickled_data = pickle.dumps(data)
        print(sys.getsizeof(pickled_data))
        data.clear()
    if xbox.get_button(7) is 1:
        exit()
