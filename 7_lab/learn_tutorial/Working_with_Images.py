import pygame 

pygame.init() 

screen = pygame.display.set_mode((700, 500))

surface = pygame.Surface((200, 100))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

image = pygame.image.load("img1.png")

clock = pygame.time.Clock() 
FPS = 60

x = 10
y = 10

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    screen.blit(image, (20, 20))
    screen.blit(surface, (70, 70))

    pygame.display.flip()
