from pygame.constants import K_RIGHT, K_UP
from map_array.map import map_array
from Core.draw_core import calculate_coard, map_compile
from Player.player import Player
from house_object.House import House
import pygame

player = Player()
#screen = 1800 * 900
WIDTH = 1800
HEIGHT = 900
WHITE = (255, 255, 255)
FPS = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))

import pygame

Map_objects = []

for y_sector in range(30):
    Building_line = []
    for x_sector in range(46):
        if map_array[y_sector, x_sector] == "Building":
            Building_line.append(House(screen, 5))

        




for i in range(player.sector - 3, player.sector + 4):
    for i in range(player.sector - 2, player.sector + 3):


pygame.init()


clock = pygame.time.Clock()
finished = False

while not finished:
    screen.fill(WHITE)
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print()
        elif event.type == pygame.MOUSEBUTTONUP:
            print()
        elif event.type == pygame.MOUSEMOTION:
            mouse_coard = event.pos
        elif event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                print("a")

    '''
    calculate_coard(objects, Player)

    for object_type in objects:
        for obj in object_type:
            obj.draw
            '''



pygame.quit()




