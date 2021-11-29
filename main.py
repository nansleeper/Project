from pygame.constants import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, K_d
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
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))

import pygame

Map_objects = []

class Road:

    def __init__(self, coard):
        self.x = coard[0]
        self.y = coard[1]



for y_sector in range(30):
    Building_line = []
    for x_sector in range(46):
        if map_array[y_sector][x_sector] == "Building":
            Building_line.append(House(screen, 10, 11, 11, (150 + x_sector * 300, 150 + y_sector * 300)))
        else:
            Building_line.append(Road((150 + x_sector * 300, 150 + y_sector * 300)))
    Map_objects.append(Building_line)
    print(len(Building_line))

print(len(Map_objects))


        




pygame.init()


clock = pygame.time.Clock()
finished = False

while not finished:
    screen.fill(WHITE)
    for x in (player.sector[0] - 3, player.sector[0] - 2,\
        player.sector[0] -1, player.sector[0], player.sector[0] + 3,\
             player.sector[0] + 2, player.sector[0] + 1):
        for y in (player.sector[1] - 1,\
            player.sector[1] + 1, player.sector[1]):
                if type(Map_objects[y][x]) != Road:
                    Map_objects[y][x].move((player.x, player.y))
                    Map_objects[y][x].draw((900, 450, 1000))
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
                player.vx = 30
            elif event.key == K_ESCAPE:
                finished = True
            elif event.key == K_LEFT:
                player.vx = - 30
            elif event.key == K_DOWN:
                player.vy = 30
            elif event.key == K_UP:
                player.vy = - 30
        elif event.type == pygame.KEYUP:
            if event.key == K_RIGHT:
                player.vx = 0
            elif event.key == K_LEFT:
                player.vx = 0
            elif event.key == K_DOWN:
                player.vy = 0
            elif event.key == K_UP:
                player.vy = 0
    player.move()
    print(player.sector)

    '''
    calculate_coard(objects, Player)

    for object_type in objects:
        for obj in object_type:
            obj.draw
            '''



pygame.quit()




