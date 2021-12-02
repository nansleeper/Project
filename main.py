from pygame.constants import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, K_d
from map_array.map import map_array
from Core.draw_core import calculate_coard, map_compile
from Player.player import Player
from house_object.House import House
from Road.road import Road
import pygame

player = Player()
#screen = 1800 * 900
WIDTH = 1800
HEIGHT = 1000
WHITE = (255, 255, 255)
FPS = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))

import pygame

Map_objects = []

house_tex =('Road/kysha.bmp', 'Road/fon.bmp')


for y_sector in range(31):
    Building_line = []
    for x_sector in range(47):
        if map_array[y_sector][x_sector] == "Building":
            Building_line.append(House(screen, 5, 12, 9,\
                 (150 + x_sector * 300, 150 + y_sector * 300), house_tex))
        else:
            Building_line.append(Road(screen, (150 + x_sector * 300,\
                 150 + y_sector * 300)))
    Map_objects.append(Building_line)





        




pygame.init()


clock = pygame.time.Clock()
finished = False

while not finished:
    screen.fill(WHITE)
    for x in (player.sector[0] - 3, player.sector[0] - 2,\
        player.sector[0] -1, player.sector[0] + 3,\
             player.sector[0] + 2, player.sector[0] + 1, player.sector[0]):
        for y in (player.sector[1] - 1,\
            player.sector[1] + 2, player.sector[1] + 1, player.sector[1]):
                Map_objects[y][x].move((player.x, player.y))
                if type(Map_objects[y][x]) == type(Map_objects[1][1]):
                    Map_objects[y][x].draw((900, 500, 600))
                else:
                    Map_objects[y][x].draw()
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1800, 150), 0)
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
                player.vx = 10
            elif event.key == K_ESCAPE:
                finished = True
            elif event.key == K_LEFT:
                player.vx = - 10
            elif event.key == K_DOWN:
                player.vy = 10
            elif event.key == K_UP:
                player.vy = - 10
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

    '''
    calculate_coard(objects, Player)

    for object_type in objects:
        for obj in object_type:
            obj.draw
    '''
    



pygame.quit()




