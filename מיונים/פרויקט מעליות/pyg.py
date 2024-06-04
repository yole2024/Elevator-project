import pygame
from setings import *
import sys
from building import building


FLOOR_HEIGHT = 50
ELEVATOR_HEIGHT = 50
SPEED = 0.5
STOP_TIME = 2
ELEVATOR_WIDTH = 50
background_color = (20,150, 20)
black = (0,0,0)







pygame.init()
size = (WIDTH,HEIGHT )
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Elevator project")
buid = building()




finish = False
while not finish:
    screen.fill(background_color )
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
            pygame.draw.rect(screen,black , pygame.Rect(1, 1, 150, 60),  2)

   
    buid.drow(screen)  
    pygame.display.update()
