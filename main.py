from map_array.map import map_array
from Core.object_core import objects
from Core.draw_core import calculate_coard, map_compile

import pygame

#screen = 1800 * 900
WIDTH = 1800
HEIGHT = 900
WHITE = (255, 255, 255)
FPS = 30

Player_x = 0
Player_y = 0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


clock = pygame.time.Clock()


while not finished:
    screen.fill(WHITE)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print()
        elif event.type == pygame.MOUSEBUTTONUP:
            print()
        elif event.type == pygame.MOUSEMOTION:
            print()

    calculate_coard(objects, Player)

    for object_type in objects:
        for obj in object_type:
            obj.draw



pygame.quit()




