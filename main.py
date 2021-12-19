from pygame.constants import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, K_a, K_d, K_KP_ENTER, K_m, K_s, K_w, K_f
from map_array.globalmap import main_map
from Core.draw_core import *
from Player.player import Player
import pygame
from Menu.menu import Menu
from Core.car import Car
from Player.info_bar import show_infobar
import math 
import random
from people.people import *

pygame.mixer.init()
player = Player()
cars = []
dv = [0, 0, 0, 0]
playerstatus = False
#screen = 1800 * 1000 and 48 * 33 map
WIDTH = 1800
HEIGHT = 1000
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 15
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

for ysector in range(33):
    for xsector in range(48):
        if str(Map_objects[ysector][xsector]) == "cross":
            Map_objects[ysector][xsector].parametrs(Map_objects)


pygame.init()


clock = pygame.time.Clock()
finished = False
menu_pos = 0
gamestatus = 'new'
cars = []

'''
for i in range(6):
    cars.append(Car(screen, [2000, 2000], 0))
    cars[i].t_unload = 2000
'''




while not finished:
    Map_activesectors = []
    Map_unloadsectors = []
    while menu.status:
        menu.draw(gamestatus)
        pygame.display.update()
    screen.fill(WHITE)
    if menu.finished:
        finished = menu.finished
        break
    gamestatus = 'continue'

    for x in (player.sector[0] - 3, player.sector[0] - 2, player.sector[0] - 1, player.sector[0] + 3, player.sector[0] + 2, player.sector[0] + 1, player.sector[0]):
        for y in (player.sector[1] - 2, player.sector[1] - 1, player.sector[1] + 2, player.sector[1] + 1, player.sector[1]):
                Map_activesectors.append(Map_objects[y][x])
    """
    # Iterate over sectors immediately behind the active ones,
    # generating people there.       
    for x in (player.sector[0] - 4, player.sector[0] + 4):
        for y in (player.sector[1] - 3, player.sector[1] + 3):
            print(x, y)
            coardx = Map_objects[y][x].cent[0] + 100
            coardy = Map_objects[y][x].cent[1] + 100
            People.people.birth(coardx, coardy)
            # Generate a couple of people sometimes.
            if random.choice([True, False]):
                x -= 30
                People.people.birth(x, y)
    """

    for i in range(len(Map_activesectors)):
        Map_activesectors[i].move((player.x, player.y))
        Map_activesectors[i].draw()
      

    for i in range(9):
        Map_unloadsectors.append(Map_objects[player.sector[1] - 3][player.sector[0] - 4 + i])

        Map_unloadsectors.append(Map_objects[player.sector[1] + 3][player.sector[0] - 4 + i])

        Map_unloadsectors[i * 2].move((player.x, player.y))
        Map_unloadsectors[i * 2 + 1].move((player.x, player.y))

    for i in range(5):
        Map_unloadsectors.append(Map_objects[player.sector[1] - 2 + i][player.sector[0] - 4])
        Map_unloadsectors.append(Map_objects[player.sector[1] - 2 + i][player.sector[0] + 4])

        Map_unloadsectors[18 + i * 2].move((player.x, player.y))
        Map_unloadsectors[19 + i * 2].move((player.x, player.y))

    for i in range(len(Map_unloadsectors)):
        if str(Map_unloadsectors[i]) == "hor" or str(Map_unloadsectors[i]) == "vert":
            if len(cars) <= 30:
              cars.append(Map_unloadsectors[i].spawncar(screen))
    
    for obj in cars:
        if str(Map_objects[obj.sector[1]][obj.sector[0]]) == "hor":
            
            obj.rotate = False
            obj.traectory[0] = obj.globalcent[0] + 2 * obj.v * math.sin(obj.angle / 180 * math.pi)
            obj.traectory[1] = Map_objects[obj.sector[1]][obj.sector[0]].globalcent[1] + \
                37 * abs(math.sin(obj.angle / 180 * math.pi)) / math.sin(obj.angle / 180 * math.pi)
            obj.traectory[2] = (360 - 90 * abs(math.sin(obj.angle / 180 * math.pi)) / \
                math.sin(obj.angle / 180 * math.pi)) % 360
            
        elif str(Map_objects[obj.sector[1]][obj.sector[0]]) == "vert":
            obj.rotate = False
            obj.traectory[1] = obj.globalcent[0] + 2 * obj.v * math.cos(obj.angle / 180 * math.pi)
            obj.traectory[0] = Map_objects[obj.sector[1]][obj.sector[0]].globalcent[0] + \
                37 * abs(math.cos(obj.angle / 180 * math.pi)) / math.cos(obj.angle / 180 * math.pi)
            obj.traectory[2] = (90 - 90 * abs(math.cos(obj.angle / 180 * math.pi)) / \
                math.cos(obj.angle / 180 * math.pi))
        elif str(Map_objects[obj.sector[1]][obj.sector[0]]) == "cross":
            '''if obj.rotate == False:
                choices = []
                for k in range(4):
                    if Map_objects[obj.sector[1]][obj.sector[0]].ways[1][k] == True:
                        choices.append(Map_objects[obj.sector[1]][obj.sector[0]].ways[1][k])
                traectory = choice(choices)
                obj.traectory = [traectory[0], traectory[1], traectory[2]]
            '''
            obj.rotate = True
        else:
            cars.pop(cars.index(obj))


  


    show_infobar(screen, player)
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
            if event.key == K_d:
                player.vx = player.v
                dv[1] = 1
            elif event.key == K_m:
                menu.mapstatus = True
                while menu.mapstatus:
                    menu.open_map()
            elif event.key == K_ESCAPE:
                if menu.status:
                    menu.status = False
                else:
                    menu.status = True
            elif event.key == K_a:
                player.vx = - player.v
                dv[3] = 1
            elif event.key == K_s:
                player.vy = player.v
                dv[2] = 1
            elif event.key == K_w:
                player.vy = - player.v
                dv[0] = 1
            elif event.key == K_f and player.car:
                player.car = False
            elif event.key == K_f and not(player.car):
                player.car = True
        elif event.type == pygame.KEYUP:
            if event.key == K_d:
                player.vx = 0
                dv[1] = 0
            elif event.key == K_a:
                player.vx = 0
                dv[3] = 0
            elif event.key == K_s:
                player.vy = 0
                dv[2] = 0
            elif event.key == K_w:
                player.vy = 0
                dv[0] = 0
            #elif event.key == K_f:
            #    playerstatus = True
   
    player.move(Map_activesectors)
    player.draw(screen)

    for obj in cars:
        obj.move(player)
          


    pygame.display.update()
    clock.tick(FPS)
    '''
    calculate_coard(objects, Player)

    for object_type in objects:
        for obj in object_type:
            obj.draw
    '''
    



pygame.mixer.quit()
pygame.quit()




