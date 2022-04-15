import time
import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

FPS = 15

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

radius = 10
body = [[100, 100]]
block = 15
dx, dy = block, 0


def food_generator():
    food_x = 10 * round((random.randint(20, WINDOW_WIDTH - 20)) / 10)
    food_y = 10 * round((random.randint(20, WINDOW_HEIGHT - 20)) / 10)

    cond = True 
    for i in range(len(body)):
        if body[i][0] == food_x and body[i][1] == food_y:
            cond = False 
            break
    if cond == True:
        return food_x, food_y
    else:
        return food_generator()

food_x, food_y = food_generator()



score = 0
level = 1
run = True

last_key = "" 


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and last_key != "left":
                last_key = "right"
                dx = block
                dy = 0
            if event.key == pygame.K_LEFT and last_key != "right":
                last_key = "left"
                dx = -block
                dy = 0
            if event.key == pygame.K_UP and last_key != "down":
                last_key = "up"
                dx = 0
                dy = -block
            if event.key == pygame.K_DOWN and last_key != "up":
                last_key = "down"
                dx = 0
                dy = block
    

    # MOVE 
    for i in range(len(body) - 1, 0, -1):
        # print(i)
        body[i][0] = body[i - 1][0]
        body[i][1] = body[i - 1][1]
    
    body[0][0] += dx
    body[0][1] += dy

          

    # ---------------------------------------
    # these lines check boundaries
    if body[0][0] > 500:
        body[0][0] = 0

    elif body[0][0] < 0:
        body[0][0] = 500

    elif body[0][1] < 0:
        body[0][1] = 500

    elif body[0][1] > 500:
        body[0][1] = 0
    # --------------------------------------


    # --------------------------------------
    # Check for Food eating, if so, add one item to Snake body

    if (body[0][0] in range(food_x - 19, food_x + 19)) and (body[0][1] in range(food_y - 19, food_y + 19)):             
        
        body.append([0, 0])
        food_x, food_y = food_generator() 
        score += 1
        
        if score % 5 == 0: # Next level
            level += 1
            FPS += 2
        
    # --------------------------------------

    screen.fill(BLACK)

    # Draw food
    pygame.draw.circle(screen, BLUE, (food_x, food_y), radius)

    # Draw snake
    for i, (x, y) in enumerate(body):
        # print("i::   ", i)
        # print(f'(x, y):: {x, y}')

        color = RED if i == 0 else GREEN
        pygame.draw.circle(screen, color, (x, y), radius)


    font = pygame.font.SysFont("comicsansms", 20)
    text = font.render(f'Score: {score} || Level: {level} || FPS: {FPS}', True, (255, 255, 255))

    screen.blit(text, (10, 10))

    # Game Over:
    for i in range(1, len(body)):
        if body[i][0] == body[0][0] and body[i][1] == body[0][1]:
            time.sleep(1)        
            screen.fill(YELLOW)
            font = pygame.font.SysFont("comicsansms", 40)
            text = font.render('Game Over', True, GREEN)
            screen.blit(text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 200))
            
            font2 = pygame.font.SysFont("comicsansms", 30)
            text2 = font2.render(f'Score: {score} || Level: {level}', True, GREEN)
            screen.blit(text2, (WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT // 2 - 150))
            pygame.display.update()
            time.sleep(3)
            run = False

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()