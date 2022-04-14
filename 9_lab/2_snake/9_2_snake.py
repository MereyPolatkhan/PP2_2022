import pygame
import random
import time

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Surface
running = True

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WHITE_2 = (100, 100, 100)
BLUE = (0, 0, 200)
GREEN = (0, 150, 0)
RED = (150, 0, 0)
YELLOW = (255, 255, 0)


BLOCK_SIZE = 20

clock = pygame.time.Clock()
FPS = 10

def lvl(n):
  if n == 0: return "Easy"
  elif n == 1: return "Medium"
  else: return "Hard"

def draw_grid():
  for i in range(0, WINDOW_WIDTH, BLOCK_SIZE):
    for j in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
      pygame.draw.rect(screen, WHITE_2, (i, j, BLOCK_SIZE, BLOCK_SIZE), 1)


class Wall:
  def __init__(self):
    self.body = []
    self.load_wall()
  
  def load_wall(self, level=0):
    with open(f'level{level}.txt', 'r') as f:
      wall_body = f.readlines()
    
    for i, line in enumerate(wall_body):
      for j, value in enumerate(line):
        if value == '#':
          self.body.append([j, i])
  
  def draw(self):
    for x, y in self.body:
      pygame.draw.rect(screen, RED, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    
class Food:
  def __init__(self):
      self.generate_random_pos()
  
  def my_round(self, value, base=BLOCK_SIZE):
    return base * round(value / base)
  
  def generate_random_pos(self):
    self.x = self.my_round(random.randint(0, WINDOW_WIDTH - BLOCK_SIZE))
    self.y = self.my_round(random.randint(0, WINDOW_HEIGHT - BLOCK_SIZE))
  
  def draw(self):
    self.color = BLUE
    pygame.draw.rect(screen, self.color, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))


class Snake:
  def __init__(self):
      self.body = [[10, 10], [11, 10],]
      self.dx = 1
      self.dy = 0
  
  def draw(self):
    for i, (x, y) in enumerate(self.body):
      color = RED if i == 0 else GREEN
      pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
  
  def move(self):
    for i in range(len(self.body) - 1, 0, -1):
      self.body[i][0] = self.body[i - 1][0]
      self.body[i][1] = self.body[i - 1][1]

    self.body[0][0] += self.dx
    self.body[0][1] += self.dy
    

snake = Snake()
food = Food()
wall = Wall()

last_key = ""
score = 0
level = 0

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT and last_key != "left":
        last_key = "right"
        snake.dx = 1
        snake.dy = 0
      if event.key == pygame.K_LEFT and last_key != "right":
        last_key = "left"
        snake.dx = -1
        snake.dy = 0
      if event.key == pygame.K_UP and last_key != "down":
        last_key = "up"
        snake.dx = 0
        snake.dy = -1
      if event.key == pygame.K_DOWN and last_key != "up":
        last_key = "down"
        snake.dx = 0
        snake.dy = 1
      if event.key == pygame.K_SPACE:
        pass        
  
  snake.move()    

  # ---------------------------------------
  # these lines check boundaries
  if snake.body[0][0] > WINDOW_WIDTH:
    snake.body[0][0] = 0

  elif snake.body[0][1] > WINDOW_HEIGHT:
    snake.body[0][1] = 0
  
  elif snake.body[0][0] < 0:
    snake.body[0][0] = WINDOW_WIDTH
  
  elif snake.body[0][1] < 0:
    snake.body[0][1] = WINDOW_HEIGHT
  # --------------------------------------  

  # Game Over-----------------------------  
  for i in range(1, len(snake.body)):
    if snake.body[i][0] == snake.body[0][0] and snake.body[i][1] == snake.body[0][1]:
      time.sleep(0.5)
      screen.fill(YELLOW)
      font = pygame.font.SysFont("comicsansms", 40)
      text = font.render('Game Over', True, GREEN)
      screen.blit(text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 200))

      font2 = pygame.font.SysFont("comicsansms", 30)
      text2 = font2.render(f'Score: {score} || Level: {lvl(level)}', True, GREEN)
      screen.blit(text2, (WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT // 2 - 150))
      pygame.display.update()
      time.sleep(3)
      running = False
  #--------------------------------------

  screen.fill(BLACK)
  
  draw_grid()
  snake.draw()
  food.draw()
  wall.draw()
  
  if snake.body[0][0] * BLOCK_SIZE == food.x and snake.body[0][1] * BLOCK_SIZE == food.y:
    snake.body.append([0, 0])
    food.generate_random_pos()
    score += 1
    if score == 10:
      level += 1
      wall.load_wall(level)
    if score == 20:
      level += 1
      wall.load_wall(level)

    if score == 5:
      food.generate_random_pos() 
      food.color = RED 
      food.draw() 
      

  font = pygame.font.SysFont("comicsansms", 20)
  text = font.render(f'Score: {score} || Level: {lvl(level)} || FPS: {FPS}', True, YELLOW)
  
  screen.blit(text, (20, 20))
  
  pygame.display.update()
  clock.tick(FPS)