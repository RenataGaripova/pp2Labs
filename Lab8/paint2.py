#To draw rectangle - press LMB.
#To draw a line - hold RMB.
#To pick an eraser - hold RMB and Ctrl.
#To draw a circle - hold LMB and Alt.

import pygame
from color_palette import *

pygame.init()

#Screen variables 
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

#Some color variable
colorRECT = (255, 0, 0)
mode = 'red' 


#Clock
clock = pygame.time.Clock()

LMBpressed = False
RMBpressed = False

#Thickness of a line or figure
THICKNESS = 5
Eraser = False
Circle = False

#Coordinates
currX = 0
currY = 0

prevX = 0
prevY = 0

iterations = 0
dx = 0
dy = 0
points = []

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

done = False

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'black':
        color = (0, 0, 0)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

while not done:

    for event in pygame.event.get():
        #Determine if a letter key was pressed to change the color mode
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = 'red'
                colorRECT= colorRED
            elif event.key == pygame.K_g:
                mode = 'green'
                colorRECT = colorGREEN
            elif event.key == pygame.K_b:
                mode = 'blue'
                colorRECT = colorBLUE
            elif event.key == pygame.K_y:
                mode = 'yellow'
                colorRECT = colorYELLOW
            elif event.key == pygame.K_w:
                mode = 'white'
                colorRECT = colorWHITE
            elif event.key == pygame.K_j:
                mode = 'gray'
                colorRECT = colorGRAY
            elif event.key == pygame.K_RCTRL or event.key == pygame.K_LCTRL:
                Eraser = True
            elif event.key == pygame.K_RALT or event.key == pygame.K_LALT:
                Circle = True

        if LMBpressed:
            screen.blit(base_layer, (0, 0))

        if event.type == pygame.QUIT:
            done = True

        #Drawing a Rectangle
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
   
        if event.type == pygame.MOUSEMOTION and LMBpressed:
            print("Position of the mouse:", event.pos)
            currX = event.pos[0]
            currY = event.pos[1]
            if not Circle:
                pygame.draw.rect(screen, colorRECT, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
            else:
                pygame.draw.circle(screen, colorRECT, (currX + (currX - prevX), currY + (currY - prevY)), abs(currX - prevX), THICKNESS)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            if not Circle:
                pygame.draw.rect(screen, colorRECT, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
            else:
                pygame.draw.circle(screen, colorRECT, (currX + (currX - prevX), currY + (currY - prevY)), abs(currX - prevX), THICKNESS)
            base_layer.blit(screen, (0, 0))

        #Drawing a Line
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            print("RMB pressed!")
            RMBpressed = True

        if event.type == pygame.MOUSEMOTION and RMBpressed:
            print("Position of the mouse:", event.pos)
            position = event.pos
            points = points + [position]
            points = points[-256:]
            i = 0
            while i < len(points) - 1:
                if not Eraser:
                    drawLineBetween(screen, i, points[i], points[i + 1], THICKNESS, mode)
                else:
                    drawLineBetween(screen, i, points[i], points[i + 1], THICKNESS, 'black')
                base_layer.blit(screen, (0, 0))
                i += 1
         
        if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            print("RMB released!")
            points = []
            RMBpressed = False

        #Increasing or Reducing Thickness
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS -= 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RCTRL or event.key == pygame.K_LCTRL:
                Eraser = False
            if event.key == pygame.K_RALT or event.key == pygame.K_LALT:
                Circle = False

    pygame.display.flip()
    clock.tick(60)

