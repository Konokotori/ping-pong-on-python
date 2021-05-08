import pygame
from time import sleep
import random

pygame.init()
win = pygame.display.set_mode((600, 300))

pygame.display.set_caption("Ping Pong")




#Var's

POSX = 0
POSY = 50
WIDTH = 40
HEIGHT = 80
SPEED = 5

BS = 5

BPOSX = 560
BWIDTH = 40
BGHEIGHT = 80
BPOSY = 0

MPOSX = 300
MPOSY = 125

#Main loop start

RUN = True
while RUN:

    #Main loop end

    #Game body start
    
    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    win.fill((0,0,0))

    #Game body end
            
    #Player start

    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and POSY > 0:
        POSY -= SPEED
    if keys[pygame.K_s] and POSY < 220:
        POSY += SPEED
    
    pygame.draw.rect(win, (255,255,255), (BPOSX, BPOSY, WIDTH, HEIGHT))
    pygame.display.update()

    #Ball start

    ball = pygame.draw.circle(win, (255, 255, 255), (MPOSX, MPOSY), 10)
    pygame.display.update()

    if keys[pygame.K_r]:
        MPOSY += BS
        MPOSX -= BS

    #Ball end

    #Player end

    #Bot start

    if keys[pygame.K_UP] and BPOSY > 0:
        BPOSY -= SPEED
    if keys[pygame.K_DOWN] and BPOSY < 220:
        BPOSY += SPEED

    
    pygame.draw.rect(win, (255,255,255), (POSX, POSY, WIDTH, HEIGHT))
    pygame.display.update()
    
    #Bot end
pygame.quit()
