import pygame 

pygame.init() 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((800, 500)) 
running = True

pygame.mixer.music.load("game_music.mp3")
pygame.mixer.music.play()

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END) 

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.mixer.music.stop() 
        
        if event.type == SONG_END:
            print("the song ended")

    
    
    pygame.display.flip()

