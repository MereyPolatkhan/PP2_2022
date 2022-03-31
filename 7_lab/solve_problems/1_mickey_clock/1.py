import pygame 
import datetime
pygame.init() 

w = (800, 600)
screen = pygame.display.set_mode(w) 

# images 
mickey = pygame.image.load("mivk.png")
background_img = pygame.transform.scale(mickey, w)

left_sec_img = pygame.image.load("ruka1.png").convert_alpha()
right_min_img = pygame.image.load("ruka2.png").convert_alpha()

font = pygame.font.SysFont("comicsansms", 30) 
text = font.render("Hello I am Mickey Mouse", True, (0, 255, 255), (0, 0, 0)) 

font2 = pygame.font.SysFont("comicsansms", 30)


def blitRotate(surf, image, pos, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = pos).center)
    surf.blit(rotated_image, new_rect.topleft)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    screen.blit(background_img, (0, 0))
    screen.blit(text, (230, 0))

    now = datetime.datetime.now() 
    position = (250, 150)
    
    # left_hand for seconds
    blitRotate(screen, left_sec_img, position, (-1) * now.second * 6)

    # right_hand for minutes 
    blitRotate(screen, right_min_img, position, (-1) * now.minute * 6)

    text2 = font2.render(f"{now.hour}:{now.minute}:{now.second}", True, (255, 0, 255), (0, 0, 0))
    screen.blit(text2, (350, 550))
    pygame.display.flip()