import pygame
from setings import *
import sys
from building import *




pygame.init()
size = (WIDTH,HEIGHT )
screen = pygame.display.set_mode(size)
#pygame.display.set_caption("Elevator project")
buid = building()




finish = False
while not finish:
    screen.fill(background_color )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

    buid.drow(screen)  
    pygame.display.update()
