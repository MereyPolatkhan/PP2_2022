import pygame 

pygame.init() 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((1000, 800)) 

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        pygame.draw.rect(screen, BLUE, pygame.Rect(10, 10, 100, 100), 10)
        
        pygame.draw.circle(screen, RED, (120, 120), 30, 10)

        pygame.draw.polygon(screen, WHITE, [(573, 235), (617, 235), (617, 462), (573, 462)],True)

        pygame.display.flip() 






