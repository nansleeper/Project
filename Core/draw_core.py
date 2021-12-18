import pygame
from random import choice
#from Core.car import Car

class Drawableobject:

    def __init__(self, screen, sector, tex = 0):
        self.cent = (sector[0] * 300 + 150, sector[1] * 300 + 150)
        self.sector = sector
        self.globalcent = (self.cent[0], self.cent[1])
        self.screen = screen
        self.tex = tex
        self.hitbox = (0, 0)
        self.name = 'Drawable.object'
        self.time = 0

    
    def __str__(self):
        return self.name
    



    def move(self, player_coord):
            '''
            Пересчитывает координаты дома в систему отсчёта игрока
            player_coord - коррдинаты игрока, двумерный список/кортеж
            '''
            System_coord = (player_coord[0] - 900, player_coord[1] - 500)
            self.cent = (self.globalcent[0] - System_coord[0],\
                self.globalcent[1] - System_coord[1])
            self.time += 1
    
    def draw(self):
        tex = pygame.image.load(self.tex)
        self.screen.blit(tex, (self.cent[0] - 150, self.cent[1] - 150))

    

win = 20 #ширина окон
brdr = 5 #ширина края дома
height = 40 #высота этажа
spect = 1000 #высота обзора
FPS = 30


class House(Drawableobject):
        def __init__(self, screen, sector, model):
            '''Класс домов, переменные:
            screen - экран на котором дом отображается
            floors - высота дома в этажах
            xwin, ywin - количество окон помещающееся на этаже,
            по оси х и у соответсвенно
            cent - координаты центра - список/кортеж из двух эл-тов
            doors - координаты на месте которых будут двери, по правой, нижней, левой и верзней стене,
            указываеться в таких же координатах
            textures - back '''

            super().__init__(screen, sector)

            self.name = "House"
            self.floors = 6
            self.z = self.floors * height + 2 * brdr
            self.xwin = 8
            self.x = 8 * win + 2 * brdr
            self.ywin = 8
            self.y = 8 * win + 2 * brdr
            self.color_win = (210, 240, 240)
            self.model = model
            self.hitbox = (self.x / 2, self.y / 2)
            if self.model == 1:
                self.color_wall = (157, 158, 152)
                self.textures = ('Core/texture/roof1.bmp', 'Core/texture/Walk_road.bmp')
            elif self.model == 2:
                self.color_wall = (159, 104, 74)
                self.textures = ('Core/texture/roof2.bmp', 'Core/texture/Walk_road.bmp')
            elif self.model == 3:
                self.color_wall = (116, 106, 104)
                self.textures = ('Core/texture/roof3.bmp', 'Core/texture/Walk_road.bmp')


            

        def draw_roof(self, spect_coord):
            '''
            :param spect_coor - список/кортеж из трех элементов - трехмерных координат точки наблюдения
            отрисовывает крышу
            '''

            
            roof = [[self.cent[0] + 0.5*self.x, self.cent[1] + 0.5*self.y, self.z],
                    [self.cent[0] + 0.5*self.x, self.cent[1] - 0.5*self.y, self.z],
                    [self.cent[0] - 0.5*self.x, self.cent[1] - 0.5*self.y, self.z],
                    [self.cent[0] - 0.5*self.x, self.cent[1] + 0.5*self.y, self.z]]
            for i in range(len(roof)):
                roof[i] = proect(roof[i], spect_coord)
            tex = pygame.image.load(self.textures[0])
            tex = pygame.transform.scale(tex, (roof[1][0] - roof[2][0], roof[0][1] - roof[1][1]))
            self.screen.blit(tex, (roof[2]))

        def draw_xwall(self, spect_coord):
            '''
            :param spect_coor - список/кортеж из трех элементов - трехмерных координат точки наблюдения
            отрисовывает левую/правую стену
            '''
            if spect_coord[0] > self.cent[0]:
                xwall = [[self.cent[0] + 0.5*self.x, self.cent[1] + 0.5*self.y, 0],
                    [self.cent[0] + 0.5*self.x, self.cent[1] - 0.5*self.y, 0],
                    [self.cent[0] + 0.5*self.x, self.cent[1] - 0.5*self.y, self.z],
                    [self.cent[0] + 0.5*self.x, self.cent[1] + 0.5*self.y, self.z]]
            else:
                xwall = [[self.cent[0] - 0.5 * self.x, self.cent[1] + 0.5 * self.y, 0],
                    [self.cent[0] - 0.5 * self.x, self.cent[1] - 0.5 * self.y, 0],
                    [self.cent[0] - 0.5 * self.x, self.cent[1] - 0.5 * self.y, self.z],
                    [self.cent[0] - 0.5 * self.x, self.cent[1] + 0.5 * self.y, self.z]]

            for i in range(len(xwall)):
                xwall[i] = proect(xwall[i], spect_coord)
            pygame.draw.polygon(self.screen, self.color_wall, xwall)
            pygame.draw.polygon(self.screen, (0, 0, 0), xwall, 1)
            
            
            for i in range(self.floors):
                for j in range(self.ywin):

                    window = [[xwall[0][0], win//5 + brdr + j * win + xwall[1][1], height//3 + brdr + i * height],
                            [xwall[0][0], 4*win//5 + brdr + j * win + xwall[1][1], height//3 + brdr + i * height],
                            [xwall[0][0], 4*win//5 + brdr + j * win + xwall[1][1], height//3 + brdr + height//2 + i * height],
                            [xwall[0][0], win//5 + brdr + j * win + xwall[1][1], height//3 + brdr + height//2 + i * height]]
                    for k in range(len(window)):
                        window[k] = proect(window[k], spect_coord)
                    pygame.draw.polygon(self.screen, self.color_win, window)
                    pygame.draw.polygon(self.screen, (0, 0, 0), window, 1)


        def draw_ywall(self, spect_coord):
            '''
            :param spect_coor - список/кортеж из трех элементов - трехмерных координат точки наблюдения
            отрисовывает верхнюю/нижнюю стену
            '''
            if spect_coord[1] > self.cent[1]:
                ywall = [[self.cent[0] + 0.5*self.x, self.cent[1] + 0.5*self.y, 0],
                    [self.cent[0] - 0.5*self.x, self.cent[1] + 0.5*self.y, 0],
                    [self.cent[0] - 0.5*self.x, self.cent[1] + 0.5*self.y, self.z],
                    [self.cent[0] + 0.5*self.x, self.cent[1] + 0.5*self.y, self.z]]
            else:
                ywall = [[self.cent[0] + 0.5 * self.x, self.cent[1] - 0.5 * self.y, 0],
                    [self.cent[0] - 0.5 * self.x, self.cent[1] - 0.5 * self.y, 0],
                    [self.cent[0] - 0.5 * self.x, self.cent[1] - 0.5 * self.y, self.z],
                    [self.cent[0] + 0.5 * self.x, self.cent[1] - 0.5 * self.y, self.z]]

            for i in range(len(ywall)):
                ywall[i] = proect(ywall[i], spect_coord)
            pygame.draw.polygon(self.screen, self.color_wall, ywall)
            pygame.draw.polygon(self.screen, (0, 0, 0), ywall, 1)

            for i in range(self.floors):
                for j in range(self.xwin):
                    window = [[win//5 + brdr + j * win + ywall[1][0], ywall[0][1], height//3 + brdr + i * height],
                            [4*win//5 + brdr + j * win + ywall[1][0], ywall[0][1], height//3 + brdr + i * height],
                            [4*win//5 + brdr + j * win + ywall[1][0], ywall[0][1], height//3 + brdr + height//2 + i * height],
                            [win//5 + brdr + j * win + ywall[1][0], ywall[0][1], height//3 + brdr + height//2 + i * height]]
                    for k in range(len(window)):
                        window[k] = proect(window[k], spect_coord)
                    pygame.draw.polygon(self.screen, self.color_win, window)
                    pygame.draw.polygon(self.screen, (0, 0, 0), window, 1)

        def draw(self, spect_coord = (900, 500, 700)):
            '''
            :param spect_coor - список/кортеж из трех элементов - трехмерных координат точки наблюдения
            отрисовывает дом вцелом, вызывая функции в правильном порядке
            '''
            tex = pygame.image.load(self.textures[1])
            self.screen.blit(tex, (self.cent[0] - 150, self.cent[1] - 150))
            if (self.cent[0] - spect_coord[0]) ** 2 > (self.cent[1] - spect_coord[1])**2:
                self.draw_ywall(spect_coord)
                self.draw_xwall(spect_coord)
            else:
                self.draw_xwall(spect_coord)
                self.draw_ywall(spect_coord)
            self.draw_roof(spect_coord)


def proect(coord, spect_coord = (900, 500, 1000)):
    '''Проецирует точку трехмерную на плоскость двумерную
    coord - трехмерные координаты точки
    spect_coord - трехмерные координаты точки, с которой мы смотрим на объект'''
    xn = coord[0] - spect_coord[0]
    yn = coord[1] - spect_coord[1]
    xn = xn*(spect_coord[2] / (spect_coord[2] - coord[2])) + spect_coord[0]
    yn = yn*(spect_coord[2] / (spect_coord[2] - coord[2])) + spect_coord[1]
    ncoord = (int(xn), int(yn))
    return(ncoord)

class Road(Drawableobject):

    def __init__(self, screen, sector, orient, ability):

        'orientation - vert, hor or cross'


        super().__init__(screen, sector)
        self.name = orient
        if orient == "hor":
            self.ways = (True, False, True, False)
            self.tex = 'Core/texture/hor.bmp'
        elif orient == "vert":
            self.ways = (False, True, False, True)
            self.tex = 'Core/texture/vert.bmp'
        elif orient == "cross":
            self.tex = 'Core/texture/cross.bmp'
            self.ways = [[True, True, True, True], [0, 0, 0, 0]]
            self.movestatus = True
        self.able = ability

    def parametrs(self, maparray):
        if str(maparray[self.sector[1] - 1][self.sector[0]]) == 'vert':
            if maparray[self.sector[1] - 1][self.sector[0]].able == True:
                self.ways[0][0] = True
                self.ways[1][0] = (maparray[self.sector[1] - 1][self.sector[0]].globalcent, 0)
            else:
                self.ways[0][0] = False
                self.ways[0][1] = False
        if str(maparray[self.sector[1] + 1][self.sector[0]]) == 'vert':
            if maparray[self.sector[1] + 1][self.sector[0]].able == True:
                self.ways[0][2] = True
                self.ways[1][2] = (maparray[self.sector[1] - 1][self.sector[0]].globalcent, 180)
            else:
                self.ways[0][2] = False
                self.ways[0][1] = False
        if str(maparray[self.sector[1]][self.sector[0] + 1]) == 'hor':
            if maparray[self.sector[1]][self.sector[0] + 1].able == True:
                self.ways[0][1] = True
                self.ways[1][1] = (maparray[self.sector[1] - 1][self.sector[0]].globalcent, 90)
            else:
                self.ways[0][1] = False
                self.ways[0][1] = False
        if str(maparray[self.sector[1]][self.sector[0] - 1]) == 'hor':
            if maparray[self.sector[1]][self.sector[0] - 1].able == True:
                self.ways[0][3] = True
                self.ways[1][3] = (maparray[self.sector[1] - 1][self.sector[0]].globalcent, 270)
            else:
                self.ways[0][3] = False
                self.ways[0][1] = False

        def spawncar(self, cars):
            i = 0
            for obj in cars:
                i += 1
                if obj.t_unable > 200 or abs(obj.cent[0] - 900) < 1200 or abs(obj.cent[1] - 500 < 800):
                    if self.name == 'hor':
                        if self.cent > 900:
                            cars[i] = Car(self.globalcent[0], self.globalcent[1] - 37)
                            cars[i].angle = 270
                        else:
                            cars[i] = Car(self.globalcent[0], self.globalcent[1] + 37)
                            self.angle = 90
                    if self.name == 'vert':
                        if self.cent > 500:
                            cars[i] = Car(self.globalcent[0] + 37, self.globalcent[1])
                            cars[i].angle = 0
                        else:
                            cars[i] = Car(self.globalcent[0] - 37, self.globalcent[1])
                            self.angle = 180
        def move(self, player_coord):
            '''
            Пересчитывает координаты дома в систему отсчёта игрока
            player_coord - коррдинаты игрока, двумерный список/кортеж
            '''
            System_coord = (player_coord[0] - 900, player_coord[1] - 500)
            self.cent = (self.globalcent[0] - System_coord[0],\
                self.globalcent[1] - System_coord[1])
            self.time += 1
            if self.time % 200 < 40:
                self.angle = 0
            elif self.time % 200 < 90 and self.time % 200 > 100:
                self.angle = 90
            elif self.time % 200 < 140 and self.time % 200 > 150:
                self.angle = 180
            elif self.time % 200 < 190 and self.time % 200 > 200:
                self.angle = 270


                



        
        

class Beach(Drawableobject):

    def __init__(self, screen, sector):

        super().__init__(screen, sector)
        self.name = "Beach"
        self.tex = 'Core/texture/beach.bmp'

class Park(Drawableobject):

    def __init__(self, screen, sector):

        
        super().__init__(screen, sector)
        self.name = "Park"
        self.tex = 'Core/texture/park.bmp'

class DownBorder(Drawableobject):

    def __init__(self, screen, sector):

        
        super().__init__(screen, sector)
        self.name = "Border"
        self.tex = 'Core/texture/downborder.bmp'

class UpBorder(Drawableobject):

    def __init__(self, screen, sector):

        
        super().__init__(screen, sector)
        self.name = "Border"
        self.tex = 'Core/texture/upborder.bmp'

class LeftBorder(Drawableobject):

    def __init__(self, screen, sector):
        
        super().__init__(screen, sector)
        self.name = "Border"
        self.tex = 'Core/texture/leftborder.bmp'

class RightBorder(Drawableobject):

    def __init__(self, screen, sector):

        
        super().__init__(screen, sector)
        self.name = "Border"
        self.tex = 'Core/texture/rightborder.bmp'

class Water(Drawableobject):

    def __init__(self, screen, sector):
        super().__init__(screen, sector)
        self.name = "Water"
        self.time = 0
        self.hitbox = (150, 150)

    def move(self, player_coord):
            '''
            Пересчитывает координаты дома в систему отсчёта игрока
            player_coord - коррдинаты игрока, двумерный список/кортеж
            '''
            System_coord = (player_coord[0] - 900, player_coord[1] - 500)
            self.cent = (self.globalcent[0] - System_coord[0],\
                self.globalcent[1] - System_coord[1])
            self.time += 1
        
    def draw(self):

        if self.time % 20 < 10:
            self.tex = 'Core/texture/water1.bmp'
        else:
            self.tex = 'Core/texture/water2.bmp'
        tex = pygame.image.load(self.tex)
        self.screen.blit(tex, (self.cent[0] - 150, self.cent[1] - 150))

class WalkingRoad(Drawableobject):

    def __init__(self, screen, sector):

        
        super().__init__(screen, sector)
        self.name = "WalkingRoad"
        self.tex = 'Core/texture/Walk_road.bmp'

class Bridge(Drawableobject):

    def __init__(self, screen, sector):

        
        super().__init__(screen, sector)
        self.name = "Bridge"
        self.tex = 'Core/texture/bridge.bmp'
