import pygame
pygame.init()

HEIGHT = 500
WIDTH = 700

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")

FPS = 60

WHITE = (255,255,255)
BLACK = (255,255,255)

class Paddle:
    COLOR = WHITE
    def __init__(self, x ,y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        def draw(self, WINDOW):
            pygame.draw.rectangle(win, self.COLOR, (self.x, self.y, self.width, self.height))

def draw(win):
    win.fill(BLACK)
    pygame.display.update()

def main ():
    run = True
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(FPS)
        draw(WINDOW)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
    pygame.quit()
        
        
if __name__ == '__main__':
    main()