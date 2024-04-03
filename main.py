import pygame
from pygame.locals import *
import time

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

class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE] * self.length
        self.y = [SIZE] * self.length
        self.direction = 'down'
        
    def draw(self):
        self.parent_screen.fill((0, 0, 0))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i])) 
        pygame.display.flip()
        
    def move_left(self):
        self.direction = 'left'
    
    def move_right(self):
        self.direction = 'right'
    
    def move_up(self):
        self.direction = 'up'
    
    def move_down(self):
        self.direction = 'down' 
     
    def walk(self):
    # kolejny blok przyjmuje współrzędne poprzedniego
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        self.draw()   

class Game:
    def __init__(self):            
        pygame.init()  
        self.board = pygame.display.set_mode((1200, 800))
        self.board.fill((0, 0, 0))
        self.snake = Snake(self.board, 5)
        self.snake.draw()
        self.food = Food(self.board)
        self.food.draw()
        
    def play(self):
        self.snake.walk()
        self.food.draw()
        
        
    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_w:
                        self.snake.move_up()
                    if event.key == K_s:
                        self.snake.move_down()
                    if event.key == K_a:
                        self.snake.move_left()
                    if event.key == K_d:
                        self.snake.move_right()
                
                        
                        
                if event.type == QUIT:
                    running = False   

            self.play()
            time.sleep(0.2)
            
if __name__ == '__main__':
    

    game = Game()
    game.run()

    pygame.display.flip()

    
