import pygame
from settings import *
from building import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# create the game building
building = Building(NUM_OF_FLOORS, NUM_OF_ELEVATORS)

pygame.display.flip()



run = True
while run :
    screen.fill(COLOR) 
    building.draw(screen, FLOOR_SPACER_HEIGHT)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            building.ide(x, y)


    pygame.display.flip()
            
