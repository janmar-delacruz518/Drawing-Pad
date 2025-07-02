import pygame
from pygame.locals import *

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing Pad")

drawing = False
last_pos = None
brush_size = 55

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen.fill(WHITE)

run = True
while run:

    for event in pygame.event.get():
        
        if event.type == QUIT:
            run = False

        if event.type == MOUSEBUTTONDOWN:
            drawing = True
            # last_pos = pygame.mouse.get_pos()
            last_pos = event.pos

        if event.type == MOUSEBUTTONUP:
            drawing = False
            last_pos = None

        if event.type == KEYDOWN and event.key == K_c:
            screen.fill(WHITE)

    if drawing and pygame.mouse.get_pressed():
        mouse_pos = pygame.mouse.get_pos()
        if last_pos:
            pygame.draw.line(screen, BLACK, last_pos, mouse_pos, brush_size)
            # pygame.draw.circle(screen, BLACK, (5, 5), True)                           # under construction
        last_pos = mouse_pos

    pygame.display.update()

pygame.quit()