import pygame
pygame.init()

HEIGHT = 500
WIDTH = 700

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")

FPS = 60

WHITE = (255,255,255)
BLACK = (255,255,255)

PADDLE_HEIGHT = 100
PADDLE_WIDTH = 20

class Paddle:
    COLOR = WHITE
    def __init__(self, x ,y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        def draw(self, WINDOW):
            pygame.draw.rect (win, self.COLOR, (self.x, self.y, self.width, self.height))

def draw(win, paddles):
    win.fill(BLACK)
    
    for Paddle in paddles:
        Paddle.draw(WINDOW)
    
    pygame.display.update()

def main ():
    run = True
    clock = pygame.time.Clock()
    
    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    
    while run:
        clock.tick(FPS)
        draw(WINDOW, [left_paddle, right_paddle])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
    pygame.quit()
        
        
if __name__ == '__main__':
    main()