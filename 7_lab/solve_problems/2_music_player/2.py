import pygame

pygame.init() 

screen = pygame.display.set_mode((480, 300)) 

kuis = ["Adai.mp3", "Balbyrauyn.mp3", "Erke_sylqym.mp3", "Sary_arka.mp3"]

def play():
    pygame.mixer.music.load(kuis[0])
    pygame.mixer.music.play(0)

# SONG_END = pygame.USEREVENT + 1
# pygame.mixer.music.set_endevent(SONG_END)

running = True 
k = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # pause/unpause
                k += 1
                if k % 2 == 1:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()


            if event.key == pygame.K_p: 
                # play
                play()                 
            
            if event.key == pygame.K_s:
                # stop
                pygame.mixer.music.stop()  

            if event.key == pygame.K_RIGHT:
                pygame.mixer.music.stop()
                # next
                kuis = kuis[1:] + [kuis[0]]
                play() 
            
            if event.key == pygame.K_LEFT:
                pygame.mixer.music.stop()
                # previous 
                kuis = [kuis[-1]] + kuis[:-1]
                play()
            


    pygame.display.flip()


# if first music ended, player should turn on second automatically 