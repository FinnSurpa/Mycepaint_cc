from dis import dis
from time import sleep
import sys, time, pygame
pygame.init()

size = width, height = 1280, 720
speed = [2, 2]
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
yellow = 255, 255, 0
cyan = 0, 255, 255
pink = 255, 0, 255
orange = 255, 128, 0
purple = 128, 0, 255
color = black
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
count = 0
screen.fill(white)
draw = False
A = None
B = None
wid = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                wid += 1
                print('Width of',wid,'px')
            if event.button == 5:
                wid -= 1
                print('Width of',wid,'px')
        if wid <=0:
            wid=1
        if key_input[pygame.K_1]:
            color = black
            print('Your color is black')
        if key_input[pygame.K_0]:
            color = white
            print('Your color is white')
        if key_input[pygame.K_2]:
            color = red
            print('Your color is red')
        if key_input[pygame.K_3]:
            color = green
            print('Your color is green')
        if key_input[pygame.K_4]:
            color = blue
            print('Your color is blue')
        if key_input[pygame.K_5]:
            color = orange
            print('Your color is orange')
        if key_input[pygame.K_6]:
            color = cyan
            print('Your color is cyan')
        if key_input[pygame.K_7]:
            color = pink
            print('Your color is pink')
        if key_input[pygame.K_8]:
            color = purple
            print('Your color is purple')
        if key_input[pygame.K_9]:
            color = yellow
            print('Your color is yellow')                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                draw = True
        if event.type == pygame.MOUSEBUTTONUP:
            draw = False
            A = None
        if draw == True:
            B = pygame.mouse.get_pos()
            if A == None:
                A = B
            pygame.draw.line(screen, color, A, B, wid)
            A = pygame.mouse.get_pos()
        pygame.display.update()
