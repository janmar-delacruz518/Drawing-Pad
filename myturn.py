import pygame                                                                           #Import Module
from pygame.locals import *

pygame.init()                                                                           # Initialize pygame

width, height = 600, 400                                                                # Screen/Window settings
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing Pad")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen fill(for screen reset) # OPTIONAL FOR VARIABLE DECLARATION
screen.fill(WHITE)

# Variables for event
drawing = False         # main event/interaction of the game
last_pos = None         # None - NoneType value
brush_size = 5

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

    if drawing and pygame.mouse.get_pressed()[0]:    # .mouse.get_pressed()[0] left mouse click
        mouse_pos = pygame.mouse.get_pos() 
        if last_pos:
            pygame.draw.line(screen, BLACK, last_pos, mouse_pos, brush_size)
        last_pos = mouse_pos

    pygame.display.update()

pygame.quit()                                                                           # Autotype for good habit