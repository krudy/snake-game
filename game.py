import pygame
from snake import Snake
from food import Food

SIZE = 40

class Game:
    def __init__(self):            
        pygame.init()  
        self.board = pygame.display.set_mode((1200, 800))
        self.board.fill((0, 0, 0))
        self.snake = Snake(self.board, 3)
        self.snake.draw()
        self.food = Food(self.board)
        self.food.draw()
        
    def play(self):
        self.snake.walk()
        self.food.draw()
        self.display_score()
        pygame.display.flip()
        
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.food.x, self.food.y):
            self.snake.increase_length()
            self.food.move()
            
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]): 
                raise "GAME OVER"
            
    def display_score(self):
        font = pygame.font.Font(None, 30)
        text = font.render("Score: " + str(self.snake.length - 3), True, (255, 255, 255))
        self.board.blit(text, (10, 10))
        pygame.display.flip()
       
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False
    
    def game_over(self):
         self.board.fill((0, 0, 0)) 
         font = pygame.font.SysFont('Helvetica',40)
         line1 = font.render('Game Over', True, (255, 10, 5))
         line2 = font.render('Press Enter to play again', True, (255, 255, 255))
         line3 = font.render(f'You have scored {self.snake.length - 1} points', True, (255, 255, 255))
         self.board.blit(line1, (500,300))
         self.board.blit(line2, (400,370))
         self.board.blit(line3, (400,440))
         pygame.display.flip()
         
    def reset(self):
        self.snake = Snake(self.board, 3)
        self.food = Food(self.board)
        
    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_RETURN:
                        pause = False
                     
                    if not pause:   
                        if event.key == pygame.K_w:
                            self.snake.move_up()
                        if event.key == pygame.K_s:
                            self.snake.move_down()
                        if event.key == pygame.K_a:
                            self.snake.move_left()
                        if event.key == pygame.K_d:
                            self.snake.move_right()
            
            try:    
                if not pause:
                    self.play()
            except Exception as e:
                self.game_over()
                pause = True
                self.reset()
                
            pygame.time.Clock().tick(10)

if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
