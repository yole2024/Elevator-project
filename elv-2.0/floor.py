import pygame.docs
from settings import *
import pygame


class Floor:
    def __init__(self, num):
        self.num = num
        self.has_elevator = True if num == 0 else False
        self.called_elevator = self.has_elevator
        self.timer = 0
        self.y = SCREEN_HEIGHT - (self.num + 1) * FLOOR_IMAGE_HEIGHT
        self.x = 0
        img = pygame.image.load(FLOOR_IMAGE_PATH)
        self.img = pygame.transform.scale(img, (FLOOR_WIDTH,FLOOR_IMAGE_HEIGHT))
        self.button = pygame.Rect(self.x,
                                  self.y + FLOOR_IMAGE_HEIGHT *0.2,
                                  FLOOR_IMAGE_HEIGHT *0.8,
                                  FLOOR_IMAGE_HEIGHT *0.8
                                   )
        self.font = pygame.font.SysFont('Arial', 25)




    def draw(self, screen, spacer):
        screen.blit(self.img, (self.x, self.y), (0, 0, FLOOR_WIDTH, FLOOR_IMAGE_HEIGHT))
        pygame.draw.line(screen, LINE_COLOR, (0, self.y + MID_SPACER ),(0 + FLOOR_WIDTH, self.y + MID_SPACER), FLOOR_SPACER_HEIGHT)
        pygame.draw.circle(screen, (BUTTON_COLOR), self.button.center,
                           self.button.width*.3)
        
        text_surface = self.font.render(f'{self.num}', True, (NUM_FLOOR_COLOR))
        screen.blit(text_surface, (self.x + 60, self.y + FLOOR_IMAGE_HEIGHT*0.3))        

        if self.timer > 0:
            timer_surface = self.font.render(f'{self.timer}', True, (BLACK))
            screen.blit(timer_surface, (self.x + 10, self.y + 40))

    def countdown_timer(self, time):
        self.timer = time

    def update_timer(self):
        if self.timer > 0:
            self.timer -= 1



    def countdown_timer(self, time):
        pass



    def is_clicked(self,x, y):
        if self.button.collidepoint(x,y):
            return self.num
        return None
