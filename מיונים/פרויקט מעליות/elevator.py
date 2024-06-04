from collections import deque
import time
from setings import *
# from floor import *
import pygame 
  
class elevator:
        def __init__(self, x, y):
            self.current_floor = 0 
            self.target_floor = None
          #  self.state = elavator_state.IDLE
            self.moving = False
            self.queue = []  #מקבל קריאות ומכניס לתור
            self.y_position = 0
            self.exit_time = None
            self.img_elevator = pygame.transform.scale(pygame.image.load(IMAGE_ELEVATOR),(50, 50))
            self.x = x 
            self.y = y 

        def update(self):
            if not self.moving and self.queue:
                 self.moving = True
                 self.exit_time = time.time()
            else:
                current_time = time.time()
                elapsed_time = current_time - self.exit_time
                  #זמן שחלף
        
        def draw_elevator( self, screen):
            screen.blit(self.img_elevator,(self.x, self.y))

                

            

        def get_final_floor(self):
            if self.queue:
                return self.queue[-1]
            return self.current_floor

        def calculate_time(self,target_floor):
            final_floor = self.get_final_floor()
            distance = abs(target_floor - final_floor)
            travel_time = distance * SPEED_PER_FLOOR
            total_time = travel_time + STOP_TIME
            return total_time
        
        def calculate_times_for_all(self, current_floor, target_floors, SPEED_PER_FLOOR, STOP_TIME):
            times = []
            for target_floor in target_floors:
                time = self.calculate_time(current_floor, target_floor, SPEED_PER_FLOOR, STOP_TIME)
                times.append(time)
            return times
        
        def move_to_floor(self, floor):
            self.queue.append(floor) 
            for i in range:
                 self

    
        