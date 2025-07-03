import pygame                                                                           #Import Module
from pygame.locals import *

pygame.init()                                                                           # Initialize pygame

width, height = 600, 400                                                                # Screen/Window settings
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing Pad")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = 0
GREEN = 0
BLUE = 0

# Screen Default
screen.fill(WHITE)

# Variables for event
drawing = False         # main event/interaction of the game
last_pos = None         # None - NoneType value
brush_size = 5
brush_color = (RED, GREEN, BLUE)

# Frame limiting for stability
clock = pygame.time.Clock()

# Monitoring Icons
circle_pos = 535
pygame.draw.circle(screen, brush_color, (circle_pos, 50), brush_size)
pygame.draw.rect(screen, (223, 197, 123), (470, 95, 121, 32))

# Screen Texts
font = pygame.font.SysFont(None, 18)

rgb_text = font.render(f"RGB: {RED}, {GREEN}, {BLUE}", True, (RED, GREEN, BLUE))
screen.blit(rgb_text, (475, 100))

brush_size_text = font.render(f"BRUSH SIZE: {brush_size}", True, (brush_size))
screen.blit(brush_size_text, (475, 112))


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
            keys = pygame.key.get_pressed()
            if keys[K_r] and event.key == K_RIGHT:        # Red    # Added RGB Adjuster       
                RED = min(255, RED + 32)
            elif keys[K_r] and event.key == K_LEFT:
                RED = max(0, RED - 32)

            if keys[K_g] and event.key == K_RIGHT:        # Green  # Added RGB Adjuster
                GREEN = min(255, GREEN + 32)
            elif keys[K_g] and event.key == K_LEFT:
                GREEN = max(0, GREEN - 32)

            if keys[K_b] and event.key == K_RIGHT:        # Blue   # Added RGB Adjuster
                BLUE = min(255, BLUE + 32)
            elif keys[K_b] and event.key == K_LEFT:
                BLUE = max(0, BLUE - 32)
            
            # Brush size adjustment

            if event.key == K_UP:
                brush_size += 1
                pygame.draw.circle(screen, WHITE, (circle_pos, 50), brush_size)
                pygame.draw.circle(screen, brush_color, (circle_pos, 50), brush_size)
            elif event.key == K_DOWN:
                brush_size = max(1, brush_size - 1) # smallest size limit 1
                pygame.draw.circle(screen, WHITE, (circle_pos, 50), brush_size + 1)
                pygame.draw.circle(screen, brush_color, (circle_pos, 50), brush_size)

            brush_color = (RED, GREEN, BLUE)
            pygame.draw.circle(screen, brush_color, (circle_pos, 50), brush_size)
            pygame.draw.rect(screen, (223, 197, 123), (470, 95, 121, 32))
            rgb_text = font.render(f"RGB: {RED}, {GREEN}, {BLUE}", True, (0, 0, 0))
            screen.blit(rgb_text, (475, 100))
            brush_size_text = font.render(f"BRUSH SIZE: {brush_size}", True, (brush_size))
            screen.blit(brush_size_text, (475, 112))

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
                pygame.draw.circle(screen, brush_color, (x, y), brush_size)
                
        last_pos = mouse_pos

    pygame.display.update()
    clock.tick(60)

pygame.quit()                                                                           # Autotype for good habit















# POSSIBLE IMPROVEMENTS
# 1. modify/improve cursor and pen position
#     - bigger line weight shows that upon drawing, the point(or shape) starts/points 
#       from the topleft corner of the pen
""" FIXED, USED CIRCLE TO DRAW INSTEAD OF RECTANGLE """
# 2. Full Screen Button/switch
# 3. Point monitor for brush color and brush size