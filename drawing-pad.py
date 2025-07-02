import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing Pad")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fill the background
screen.fill(WHITE)

# Variables
drawing = False
last_pos = None
brush_size = 5

# Main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

        # Start drawing
        if event.type == MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos

        # Stop drawing
        if event.type == MOUSEBUTTONUP:
            drawing = False
            last_pos = None

        # Clear screen with 'C' key
        if event.type == KEYDOWN:
            if event.key == K_c:
                screen.fill(WHITE)

    # Draw while moving the mouse
    if drawing and pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        if last_pos:
            pygame.draw.line(screen, BLACK, last_pos, mouse_pos, brush_size)
        last_pos = mouse_pos

    pygame.display.update()

# Quit
pygame.quit()
