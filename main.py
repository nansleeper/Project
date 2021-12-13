from pygame.constants import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, K_d, K_KP_ENTER, K_m
from map_array.globalmap import main_map
from Core.draw_core import *
from Player.player import Player
import pygame
from Menu.menu import Menu


player = Player()
#screen = 1800 * 1000 and 48 * 33 map
WIDTH = 1800
HEIGHT = 1000
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))

import pygame
menu = Menu(screen, player)
Map_objects = []

for y_sector in range(33):
    Building_line = []
    for x_sector in range(48):
        
        if main_map[y_sector][x_sector] == "House1":
            Building_line.append(House(screen, (x_sector, y_sector), 1))
        elif main_map[y_sector][x_sector] == "House2":
            Building_line.append(House(screen, (x_sector, y_sector), 2))
        elif main_map[y_sector][x_sector] == "House3":
            Building_line.append(House(screen, (x_sector, y_sector), 3))
        elif main_map[y_sector][x_sector] == "Walk_road":
            Building_line.append(WalkingRoad(screen, (x_sector, y_sector)))
        elif main_map[y_sector][x_sector] == "CrossRoad":
            Building_line.append(Road(screen, (x_sector, y_sector), "cross", True))
        elif main_map[y_sector][x_sector] == "HorRoad":
            Building_line.append(Road(screen, (x_sector, y_sector), 'hor', True))
        elif main_map[y_sector][x_sector] == "VertRoad":
            Building_line.append(Road(screen, (x_sector, y_sector), 'vert', True))
        elif main_map[y_sector][x_sector] == "HorRoadUnable":
            Building_line.append(Road(screen, (x_sector, y_sector), 'hor', False))
        elif main_map[y_sector][x_sector] == "VertRoadUnable":
            Building_line.append(Road(screen, (x_sector, y_sector), 'vert', False))
        elif main_map[y_sector][x_sector] == "DownBorder":
            Building_line.append(DownBorder(screen, (x_sector, y_sector)))
        elif main_map[y_sector][x_sector] == "LeftBorder":
            Building_line.append(LeftBorder(screen, (x_sector, y_sector)))
        elif main_map[y_sector][x_sector] == "RightBorder":
            Building_line.append(RightBorder(screen, (x_sector, y_sector)))
        elif main_map[y_sector][x_sector] == "UpBorder":
            Building_line.append(UpBorder(screen, (x_sector, y_sector)))
        elif main_map[y_sector][x_sector] == "Park":
            Building_line.append(Park(screen, (x_sector, y_sector)))
        elif main_map[y_sector][x_sector] == "Beach":
            Building_line.append(Beach(screen, (x_sector, y_sector)))
        elif main_map[y_sector][x_sector] == "Water":
            Building_line.append(Water(screen, (x_sector, y_sector)))
        elif main_map[y_sector][x_sector] == "Bridge":
            Building_line.append(Bridge(screen, (x_sector, y_sector)))
        else:
            print(main_map[y_sector][x_sector],'ERROR')
    Map_objects.append(Building_line)


pygame.init()


clock = pygame.time.Clock()
finished = False
menu_pos = 0
gamestatus = 'new'

while not finished:
    while menu.status:
        menu.draw(gamestatus)
        pygame.display.update()
    screen.fill(WHITE)
    if menu.finished:
        finished = menu.finished
        break
    gamestatus = 'continue'
    for x in (player.sector[0] - 3, player.sector[0] - 2,\
        player.sector[0] - 1, player.sector[0] + 3,\
             player.sector[0] + 2, player.sector[0] + 1, player.sector[0]):
        for y in (player.sector[1] - 2, player.sector[1] - 1,\
            player.sector[1] + 2, player.sector[1] + 1, player.sector[1]):
                Map_objects[y][x].move((player.x, player.y))
                Map_objects[y][x].draw()
    info_screen = pygame.image.load('Core/texture/fonmain.bmp')
    screen.blit(info_screen, (0, 0))
    pygame.draw.polygon(screen, (255, 250, 0),
                        ((120, 15), (172, 45), (172, 105), (120, 135), (68, 105), (68, 45), (120, 15)))
    pygame.draw.polygon(screen, (248, 250, 251),
                        ((120, 25), (163, 50), (163, 100), (120, 125), (77, 100), (77, 50), (120, 25)))
    pygame.draw.polygon(screen, (255, 165, 0),
                        ((120, 15), (172, 45), (172, 105), (120, 135), (68, 105), (68, 45), (120, 15)), 5)
    pygame.draw.rect(screen, (255, 255, 255), (200, 40, 310, 70), 3)
    pygame.draw.rect(screen, (155, 0, 0), (205, 45, 3 * player.health, 60))
    if player.car:
        icon_screen = pygame.image.load('Core/texture/carico.bmp')
        icon_screen.set_colorkey((248, 250, 251))
        screen.blit(icon_screen, (68, 30))
    elif player.fire:
        icon_screen = pygame.image.load('Core/texture/fireico.bmp')
        icon_screen.set_colorkey((255, 255, 255))
        screen.blit(icon_screen, (90, 40))
    else:
        icon_screen = pygame.image.load('Core/texture/playerico.bmp')
        icon_screen.set_colorkey((248, 250, 251))
        screen.blit(icon_screen, (70, 30))
    #pygame.display.update()
    #clock.tick(FPS)
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
            elif event.key == K_m:
                menu.mapstatus = True
                while menu.mapstatus:
                    menu.open_map()
            elif event.key == K_ESCAPE:
                if menu.status:
                    menu.status = False
                else:
                    menu.status = True
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
    player.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
    '''
    calculate_coard(objects, Player)

    for object_type in objects:
        for obj in object_type:
            obj.draw
    '''
    



pygame.quit()




