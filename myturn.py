import pygame                                                                           #Import Module
from pygame.locals import *

pygame.init()                                                                           # Initialize pygame

width, height = 600, 400                                                                # Screen/Window settings
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing Pad")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen Default
screen.fill(WHITE)

# Variables for event
drawing = False         # main event/interaction of the game
last_pos = None         # None - NoneType value
brush_size = 5
brush_color = (0)

# frame limiting for stability
clock = pygame.time.Clock()

run = True                                                                              # Main Loop for running the screen/window
while run:

    for event in pygame.event.get():

        if event.type == QUIT:
            run = False
        
        if event.type == MOUSEBUTTONDOWN:       # mouse click response
            drawing = True
            last_pos = event.pos                # .pos coordinates/position of the mouse

        if event.type == MOUSEBUTTONUP:
            drawing = False
            last_pos = None

        if event.type == KEYDOWN and event.key == K_c:      # Key response monitor for c key
            screen.fill(WHITE)

        # **************** ADDED FEATURES ***************
        if event.type == KEYDOWN:

            # Brush Color Choices
            if event.key == K_r:        # Red
                brush_color = (255, 0, 0)
            elif event.key == K_g:      # Green
                brush_color = (0, 255, 0)
            elif event.key == K_b:      # Blue
                brush_color = (0, 0, 255)
            elif event.key == K_0:      # Black
                brush_color = BLACK
            
            # Brush size adjustment
            if event.key == K_UP:
                brush_size += 1
            elif event.key == K_DOWN:
                if brush_size != 1:     # smallest size limit
                    brush_size -= 1

    if drawing and pygame.mouse.get_pressed()[0]:    # .mouse.get_pressed()[0] left mouse click

        mouse_pos = pygame.mouse.get_pos()

        if last_pos:

            # pygame.draw.line(screen, BLACK, last_pos, mouse_pos, brush_size)
            # pygame.draw.line(screen, brush_color, last_pos, mouse_pos, brush_size)
            # pygame.draw.circle(screen, brush_color, mouse_pos, brush_size)

            # Cleaner Draw of connected rectangles
            x1, y1 = last_pos
            x2, y2 = mouse_pos
            dx = x2 - x1
            dy = y2 - y1
            distance = max(abs(dx), abs(dy))

            for i in range(distance):

                x = int(x1 + float(i) / distance * dx)
                y = int(y1 + float(i) / distance * dy)
                # pygame.draw.rect(screen, brush_color, (x, y, brush_size, brush_size))
                pygame.draw.circle(screen, brush_color, (x, y,), brush_size)
                
        last_pos = mouse_pos

    pygame.display.update()
    clock.tick(60)

pygame.quit()                                                                           # Autotype for good habit

# POSSIBLE IMPROVEMENTS
# 1. modify/improve cursor and pen position
#     - bigger line weight shows that upon drawing, the point(or shape) starts/points 
#       from the topleft corner of the pen
""" FIXED, USED CIRCLE TO DRAW INSTEAD OF RECTANGLE """