import pygame 

pygame.init() 

screen = pygame.display.set_mode((640, 480)) 
clock = pygame.time.Clock() 
running = True 

GREEN = (0, 128, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont("", 100) 
# font = pygame.font.Font(None, 100)


text = font.render("Hello, World!", True, GREEN) 
# print(f'width: {text.get_width()}; height: {text.get_height()}')

# print(pygame.font.get_fonts())

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False 

    screen.fill(WHITE) 
    screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))
    pygame.display.flip() 
    clock.tick(60)
             



