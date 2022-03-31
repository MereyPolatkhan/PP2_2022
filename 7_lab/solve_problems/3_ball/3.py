import pygame

pygame.init() 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((500, 500))

clock = pygame.time.Clock() 

running = True 
color_of_ball = RED

x = 50
y = 50

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_SPACE):
            running = False 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            color_of_ball = BLUE if color_of_ball == RED else RED

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP:
        #         y = y - 20
        #         if y <= 25:
        #             y = 25
        #     if event.key == pygame.K_DOWN:
        #         y = y + 20
        #         if y >= 475:
        #             y = 475
        #     if event.key == pygame.K_RIGHT:
        #         x = x + 20
        #         if x >= 475:
        #             x = 475
        #     if event.key == pygame.K_LEFT:
        #         x = x - 20
        #         if x <= 25:
        #             x = 25

    
    pressed = pygame.key.get_pressed() 

    if pressed[pygame.K_UP] == True:
        y = y - 20
        if y <= 25:
            y = 25
    if pressed[pygame.K_DOWN] == True:
        y = y + 20
        if y >= 475:
            y = 475
    if pressed[pygame.K_RIGHT] == True:
        x = x + 20
        if x >= 475:
            x = 475
    if pressed[pygame.K_LEFT] == True:
        x = x - 20
        if x <= 25:
            x = 25

    screen.fill(WHITE) 

    pygame.draw.circle(screen, color_of_ball, (x, y), 25)

    clock.tick(60)

    pygame.display.flip() 