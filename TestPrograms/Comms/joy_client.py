import pygame, socket, shutil,sys

host = '127.0.0.1'
port = 932

s = socket.socket()
s.connect((host,port))

pygame.init() #needed for the event loop
pygame.joystick.init()
joy_count = pygame.joystick.get_count() #num of controllers connected
if joy_count==0: #controller check
    print("no controllers connected")
    exit()
#controller found
xbox = pygame.joystick.Joystick(0)
xbox.init()
print('xbox id:',xbox.get_id())
print(xbox.get_name())
print(xbox.get_numaxes(),'axes')
print(xbox.get_numballs(),'balls')
print(xbox.get_numbuttons(),"buttons")
print(xbox.get_numhats(),"hat")
while True:
    for event in pygame.event.get():
        xboxLY = str(round(xbox.get_axis(1)*-127)+127)
        encoded = xboxLY.encode() #string to bytes
        #print(sys.getsizeof(encoded))
        s.send(encoded)
        data = s.recv(1024).decode()
        print('Received from Server : ' + data)
        if xbox.get_button(7)==1:
            exit()
