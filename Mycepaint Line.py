from dis import dis
from time import sleep
import sys, time, pygame
pygame.init()

size = width, height = 1280, 720
speed = [2, 2]
white = 255, 255, 255
black = 0, 0, 0

screen = pygame.display.set_mode(size)
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
                print('Epaisseur de',wid,'px')
            if event.button == 5:
                wid -= 1
                print('Epaisseur de',wid,'px')
        if wid <=0:
            wid=1
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
            pygame.draw.line(screen, black, A, B, wid)
            A = pygame.mouse.get_pos()
        pygame.display.update()