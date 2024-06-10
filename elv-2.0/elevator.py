from settings import *
from collections import deque
import pygame

class Elevator:
    def __init__(self, num):
        self.num = num
        self.y = SCREEN_HEIGHT - ELEVATOR_HEIGHT
        self.x = num * 50 + FLOOR_WIDTH
        self.current_floor = 0
        self.tasks = deque([])
        img = pygame.image.load(ELEVATOR_IMAGE_PATH)
        self.img = pygame.transform.scale(img, (ELEVATOR_WIDTH,ELEVATOR_HEIGHT))


    def draw(self, screen):
        print(self.x,self.y)
        screen.blit(self.img, (self.x, self.y))

    def move(self, target_floor):
        pass


    def append (self, num_floor, time):
        self.tasks.append(num_floor, time)


    def get_final_floor(self):
        if self.tasks:
            return self.tasks[-1][0]
        return self.current_floor
    
    def calculate_time(self,target_floor):
        final_floor = self.get_final_floor()
        distance = abs(target_floor - final_floor)
        travel_time = distance * SECONDS_PER_FLOOR
        total_time = travel_time + STOP_TIME
        return total_time
    
    def calculate_times_for_all(self):
        if self.tasks:
            return self.tasks[-1][1]
        return 0