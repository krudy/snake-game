import pygame
import random

SIZE = 40

class Food:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/mouse.png").convert()
        self.parent_screen = parent_screen
        self.x = SIZE * 3
        self.y = SIZE * 3
    
    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y)) 
        pygame.display.flip()   
        
    def move(self):
        self.x = random.randint(0, 29) * SIZE
        self.y = random.randint(0, 19) * SIZE
