import pygame
from pygame.locals import *

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Smooth Rect Drawing")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen.fill(WHITE)

drawing = False
last_pos = None
brush_size = 10

# clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

        if event.type == MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos

        if event.type == MOUSEBUTTONUP:
            drawing = False
            last_pos = None

        if event.type == KEYDOWN and event.key == K_c:
            screen.fill(WHITE)

    if drawing and pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        if last_pos:
            # Interpolate between points
            x1, y1 = last_pos
            x2, y2 = mouse_pos

            dx = x2 - x1
            dy = y2 - y1
            distance = max(abs(dx), abs(dy))  # pixels to cover

            for i in range(distance):
                x = int(x1 + float(i) / distance * dx)
                y = int(y1 + float(i) / distance * dy)
                # pygame.draw.rect(screen, BLACK, (x, y, brush_size, brush_size))
                pygame.draw.circle(screen, BLACK, (x, y,), brush_size)

        last_pos = mouse_pos

    pygame.display.update()
    # clock.tick(60)

pygame.quit()
