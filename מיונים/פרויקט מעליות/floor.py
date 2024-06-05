import time
import pygame
from setings import *


class floor:
    def __init__(self, x, y):
        self.Timer = 0
        self.light = None
        self.img_floor = pygame.transform.scale(pygame.image.load(IMAGE_FLOOR),(FLOOR_WEIGHT,FLOOR_HEIGHT))
        self.x = x
        self.y = y


    def Displaying_the_timer(self, time):
        pass
    def display_light(self, coler):
        pass

    def countdown_timer(seconds):
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            timer = f'{mins:02d}:{secs:02d}'
            print(timer, end="\r")
            time.sleep(1)
            seconds -= 1
        print('00:00')

    def draw_floor( self, screen):
        screen.blit(self.img_floor,(self.x, self.y))

    def draw_floor_number(self):
        pass