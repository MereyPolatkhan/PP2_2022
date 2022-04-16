import pygame
import math

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
    
screen.fill((0, 0, 0))

rect_baseLayer = pygame.Surface((640, 480))
rect_prevX = -1
rect_prevY = -1
rect_currentX = -1
rect_currentY = -1
rect_isMousedown = False 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

def colors(color):
    if color == WHITE: return 'WHITE'
    if color == BLACK: return 'BLACK'
    if color == RED: return 'RED'
    if color == GREEN: return 'GREEN'
    if color == BLUE: return 'BLUE'
    

color = WHITE
radius = 5
mode = ""
font = pygame.font.SysFont("comicsansms", 20)

pen_prevX = 0
pen_prevY = 0
isMouseDown = False


# calculate Figures -------------------------------------
def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculateCircle(x1, y1, x2, y2) :
    return ( (min(x1, x2), min(y1, y2)), abs(abs(x1 - x2) - abs(y1 - y2)) )

def calculateSquare(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(x1 - x2))

def calculateRightTriangle(x1, y1, x2, y2) :
    top = (x1, y1)
    bottom = (x1, y2)
    right = (x2, y2)
    return (top, bottom, right)

def calculateEqualTriangle(x1, y1, x2, y2) :
    distance = abs(x1 - x2)
    height = math.sqrt( distance ** 2 - (distance / 2) ** 2 )
    top = (x1 + distance / 2, y1)
    left = (x1, y1 + height)
    right = (x2, y1 + height)
    return (top, left, right)

def calculateRomb(x1, y1, x2, y2) :
    top = (x1 + abs(x1 - x2) / 2, y1)
    bottom = (x1 + abs(x1 - x2) / 2, y2)
    right = (x2, y1 + abs(y1 - y2) / 2)
    left = (x1, y1 + abs(y1 - y2) / 2)
    return (top, right, bottom, left)
#----------------------------------------------------------------


run = True 
while run:
    # screen.fill(BLACK)
    pen_currentX = pen_prevX
    pen_currentY = pen_prevY
    # alt and ctrl 
    pressed = pygame.key.get_pressed()
    alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
    ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]


    for event in pygame.event.get():

        # Mouse Button---------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                isMouseDown = True
                rect_isMousedown = True 
                rect_currentX =  event.pos[0]
                rect_currentY =  event.pos[1]
                rect_prevX =  event.pos[0]
                rect_prevY =  event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP:
            rect_isMousedown = False 
            rect_baseLayer.blit(screen, (0, 0))
            if event.button == 1: 
                isMouseDown = False

        if event.type == pygame.MOUSEMOTION:
            if rect_isMousedown == True:
                rect_currentX =  event.pos[0]
                rect_currentY =  event.pos[1]
            # if mouse moved, add point to list
            pen_currentX =  event.pos[0]
            pen_currentY =  event.pos[1]
               
        #----------------------------
        
        # Close pygame---------------
        if event.type == pygame.QUIT:
                run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and ctrl_held:
                run = False
            if event.key == pygame.K_F4 and alt_held:
                run = False
            if event.key == pygame.K_ESCAPE:
                run = False
        #----------------------------

        # push r / g / b / w / y --> Color selection
        # Color selection------------ 
            if event.key == pygame.K_r and ctrl_held == False:
                # screen.fill(BLACK)
                color = RED
            if event.key == pygame.K_g:
                # screen.fill(BLACK)
                color = GREEN
            if event.key == pygame.K_b:
                # screen.fill(BLACK)
                color = BLUE
            if event.key == pygame.K_w:
                # screen.fill(BLACK)
                color = WHITE
            if event.key == pygame.K_y:
                # screen.fill(BLACK)
                color = YELLOW

        # ctrl + delete == delete all:
            if event.key == pygame.K_DELETE and ctrl_held:
                screen.fill(BLACK)

        #---------------------------

        # Radius shrink / grow------
            if event.key == pygame.K_1: 
                radius += 1
            if event.key == pygame.K_0:
                radius -= 1
        #----------------------------

        # pen / rect / circle / eraser------ 
            # push ctrl + r --> Draw rectangle
            # push ctrl + c --> Draw circle
            # push ctrl + e --> Eraser
            # push ctrl + p --> Pen

            if ctrl_held and event.key == pygame.K_r:
                # screen.fill(BLACK)
                mode = 'rectangle'
            if ctrl_held and event.key == pygame.K_c:
                # screen.fill(BLACK)
                mode = 'circle'
            if ctrl_held and event.key == pygame.K_e:
                # screen.fill(BLACK)
                mode = 'eraser'
            if ctrl_held and event.key == pygame.K_p:
                # screen.fill(BLACK)
                mode = 'pen'

            # LAB 9 tasks --> 
            # 1)square ==> alt + s 
            # 2)right triangle ==> alt + x
            # 3)equilateral triangle ==> alt y 
            # 4)rhombus ==> alt + h
            if alt_held and event.key == pygame.K_s:
                # screen.fill(BLACK)
                mode = 'square'
            if alt_held and event.key == pygame.K_x:
                # screen.fill(BLACK)
                mode = 'right tri'
            if alt_held and event.key == pygame.K_y:
                # screen.fill(BLACK)
                mode = 'eq tri'
            if alt_held and event.key == pygame.K_h:
                # screen.fill(BLACK)
                mode = 'rhombus'
            
        #------------------------------------
       
        # choose mode ---------------------------------------

        if mode == 'rectangle': # ctrl r
            if rect_isMousedown == True and rect_prevX != -1 and rect_prevY != -1 and rect_currentX != -1 and rect_currentY != -1:
                screen.blit(rect_baseLayer, (0, 0))
                r = calculateRect(rect_prevX, rect_prevY, rect_currentX, rect_currentY)
                pygame.draw.rect(screen, color,pygame.Rect(r), radius)


        if mode == 'pen': # ctrl p
            if isMouseDown == True:
                pygame.draw.line(screen, color, (pen_prevX, pen_prevY), (pen_currentX, pen_currentY), radius)
            pen_prevX = pen_currentX
            pen_prevY = pen_currentY

        if mode == 'eraser': # ctrl e
            if isMouseDown == True:
                pygame.draw.line(screen, BLACK, (pen_prevX, pen_prevY), (pen_currentX, pen_currentY), radius + 10)
            pen_prevX = pen_currentX
            pen_prevY = pen_currentY

        if mode == 'circle': # ctrl c
            if rect_isMousedown == True and rect_prevX != -1 and rect_prevY != -1 and rect_currentX != -1 and rect_currentY != -1:
                screen.blit(rect_baseLayer, (0, 0))
                r = calculateCircle(rect_prevX, rect_prevY, rect_currentX, rect_currentY)
                pygame.draw.circle(screen, color, (rect_currentX, rect_currentY), radius * 10, radius)
        #---------------------------------------------------

        # LAB 9 tasks --> 1)square, 2)right trngl, 3)eq trngl, 4)rhombus 

        if mode == 'square': # square ==> alt + s
            if rect_isMousedown == True and rect_prevX != -1 and rect_prevY != -1 and rect_currentX != -1 and rect_currentY != -1:
                screen.blit(rect_baseLayer, (0, 0))
                r = calculateSquare(rect_prevX, rect_prevY, rect_currentX, rect_currentY)
                pygame.draw.rect(screen, color,pygame.Rect(r), radius)
        
        if mode == 'right tri': # right triangle ==> alt + x
            if rect_isMousedown == True and rect_prevX != -1 and rect_prevY != -1 and rect_currentX != -1 and rect_currentY != -1:
                screen.blit(rect_baseLayer, (0, 0))
                r = calculateRightTriangle(rect_prevX, rect_prevY, rect_currentX, rect_currentY)
                pygame.draw.polygon(screen, color, r, radius)
        
        
        if mode == 'eq tri': # equilateral triangle ==> alt y
            if rect_isMousedown == True and rect_prevX != -1 and rect_prevY != -1 and rect_currentX != -1 and rect_currentY != -1:
                screen.blit(rect_baseLayer, (0, 0))
                r = calculateEqualTriangle(rect_prevX, rect_prevY, rect_currentX, rect_currentY)
                pygame.draw.polygon(screen, color, r, radius)
        
        if mode == 'rhombus': # rhombus ==> alt + h
            if rect_isMousedown == True and rect_prevX != -1 and rect_prevY != -1 and rect_currentX != -1 and rect_currentY != -1:
                screen.blit(rect_baseLayer, (0, 0))
                r = calculateRomb(rect_prevX, rect_prevY, rect_currentX, rect_currentY)
                pygame.draw.polygon(screen, color, r, radius)


    #---------------------------------
    
    pygame.display.update(0, 0, 640, 20)
    
    pygame.display.flip() 
    clock.tick(60)

        




        