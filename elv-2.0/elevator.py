from settings import *
from collections import deque
import pygame
import time

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
        screen.blit(self.img, (self.x, self.y))

    def move(self, target_floor):
        pass


    def append (self, num_floor, time):
        self.tasks.append((num_floor, time))


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
    

    def update(self):
        if not self.moving and self.tasks:
            self.target_floor = self.tasks.popleft()
            self.moving = True
            self.exit_time = time.time()
        elif self.moving:
            current_time = time.time()
            elapsed_time = current_time - self.exit_time
            travel_time = abs(self.target_floor - self.current_floor) * SECONDS_PER_FLOOR

            if elapsed_time >= travel_time + STOP_TIME:
                self.current_floor = self.target_floor
                self.moving = False
                self.exit_time = None

    #def 