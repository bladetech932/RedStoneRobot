
import pygame

fill_color = (255,255,255)
text_color = (0,0,0)
quit = False

pygame.init() #lib init not req for joystick.

pyclock = pygame.time.Clock()
pygame.joystick.init() #init for the joystick lib
joy_count = pygame.joystick.get_count() #num of controllers connected
if joy_count==0: #controller check
    print('no controllers connected')
    exit()

#print info about controller

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
        #if abs(xbox.get_axis(1))>0.05:
        print(xbox.get_axis(1))
        #pyclock.tick(20)





pygame.joystick.quit()
pygame.quit()
