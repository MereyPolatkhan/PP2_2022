import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    baseLayer = pygame.Surface((640, 480))

    clock = pygame.time.Clock()
    
    prevX = -1
    prevY = -1
    currentX = -1
    currentY = -1
        
    screen.fill((0, 0, 0))

    isMouseDown = False

    while True:
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]    
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))


            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
        

        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
            screen.blit(baseLayer, (0, 0))
            pygame.draw.circle(screen, (255, 255, 255), (currentX, currentY), 55, 1,)    

        pygame.display.flip()
        clock.tick(60)
        

main()