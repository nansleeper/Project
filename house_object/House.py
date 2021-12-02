import pygame

pygame.init()

win = 20 #ширина окон
brdr = 5 #ширина края дома
height = 40 #высота этажа
spect = 1000 #высота обзора
FPS = 30

class House:
        def __init__(self, screen, floors, xwin, ywin, cent, textures, doors = (0, 0, 0, 0)):
            '''Класс домов, переменные:
            screen - экран на котором дом отображается
            floors - высота дома в этажах
            xwin, ywin - количество окон помещающееся на этаже,
            по оси х и у соответсвенно
            cent - координаты центра - список/кортеж из двух эл-тов
            doors - координаты на месте которых будут двери, по правой, нижней, левой и верзней стене,
            указываеться в таких же координатах'''
            self.screen = screen
            self.floors = floors
            self.z = floors*height + 2*brdr
            self.xwin = xwin
            self.x = xwin*win + 2*brdr
            self.ywin = ywin
            self.y = ywin*win + 2*brdr
            self.cent = cent
            self.color_roof = (140, 140, 140)
            self.color_wall = (190, 50, 40)
            self.color_win = (210, 240, 240)
            self.color_door = (50, 20, 10)
            self.doors = doors
            self.textures = textures
            self.globalx = cent[0]
            self.globaly = cent[1]

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
            pygame.draw.polygon(self.screen, self.color_roof, roof)
            pygame.draw.polygon(self.screen, (0, 0, 0), roof, 1)

        def draw_xwall(self, spect_coord):
            '''
            :param spect_coor - список/кортеж из трех элементов - трехмерных координат точки наблюдения
            отрисовывает левую/правую стену
            '''
            if spect_coord[0] > self.cent[0]:
                door_coord = self.doors[0]
                xwall = [[self.cent[0] + 0.5*self.x, self.cent[1] + 0.5*self.y, 0],
                    [self.cent[0] + 0.5*self.x, self.cent[1] - 0.5*self.y, 0],
                    [self.cent[0] + 0.5*self.x, self.cent[1] - 0.5*self.y, self.z],
                    [self.cent[0] + 0.5*self.x, self.cent[1] + 0.5*self.y, self.z]]
            else:
                door_coord = self.doors[2]
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
                    if j == door_coord - 1 and i == 0:
                        door = [[xwall[0][0], win // 5 + brdr + j * win + xwall[1][1], i * height],
                                [xwall[0][0], 4 * win // 5 + brdr + j * win + xwall[1][1], i * height],
                                [xwall[0][0], 4 * win // 5 + brdr + j * win + xwall[1][1], 6*height//7 + i * height],
                                [xwall[0][0], win // 5 + brdr + j * win + xwall[1][1], 6*height//7 + i * height]]
                        for k in range(len(door)):
                            door[k] = proect(door[k], spect_coord)
                        pygame.draw.polygon(self.screen, self.color_door, door)
                        pygame.draw.polygon(self.screen, (0, 0, 0), door, 1)
                        continue

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
                door_coord = self.doors[1]
                ywall = [[self.cent[0] + 0.5*self.x, self.cent[1] + 0.5*self.y, 0],
                    [self.cent[0] - 0.5*self.x, self.cent[1] + 0.5*self.y, 0],
                    [self.cent[0] - 0.5*self.x, self.cent[1] + 0.5*self.y, self.z],
                    [self.cent[0] + 0.5*self.x, self.cent[1] + 0.5*self.y, self.z]]
            else:
                door_coord = self.doors[3]
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
                    if j == door_coord - 1 and i == 0:
                        door = [[win // 5 + brdr + j * win + ywall[1][0], ywall[0][1], i * height],
                                [4 * win // 5 + brdr + j * win + ywall[1][0], ywall[0][1], i * height],
                                [4 * win // 5 + brdr + j * win + ywall[1][0], ywall[0][1], 6 * height // 7 + i * height],
                                [win // 5 + brdr + j * win + ywall[1][0], ywall[0][1], 6 * height // 7 + i * height]]
                        for k in range(len(door)):
                            door[k] = proect(door[k], spect_coord)
                        pygame.draw.polygon(self.screen, self.color_door, door)
                        pygame.draw.polygon(self.screen, (0, 0, 0), door, 1)
                        continue
                    window = [[win//5 + brdr + j * win + ywall[1][0], ywall[0][1], height//3 + brdr + i * height],
                            [4*win//5 + brdr + j * win + ywall[1][0], ywall[0][1], height//3 + brdr + i * height],
                            [4*win//5 + brdr + j * win + ywall[1][0], ywall[0][1], height//3 + brdr + height//2 + i * height],
                            [win//5 + brdr + j * win + ywall[1][0], ywall[0][1], height//3 + brdr + height//2 + i * height]]
                    for k in range(len(window)):
                        window[k] = proect(window[k], spect_coord)
                    pygame.draw.polygon(self.screen, self.color_win, window)
                    pygame.draw.polygon(self.screen, (0, 0, 0), window, 1)

        def draw(self, spect_coord):
            '''
            :param spect_coor - список/кортеж из трех элементов - трехмерных координат точки наблюдения
            отрисовывает дом вцелом, вызывая функции в правильном порядке
            '''

            tex = pygame.image.load(self.textures)
            self.screen.blit(tex, (self.cent[0] - 150, self.cent[1] - 150))
            if (self.cent[0] - spect_coord[0]) ** 2 > (self.cent[1] - spect_coord[1])**2:
                self.draw_ywall(spect_coord)
                self.draw_xwall(spect_coord)
            else:
                self.draw_xwall(spect_coord)
                self.draw_ywall(spect_coord)
            self.draw_roof(spect_coord)

        def move(self, player_coord):
            '''
            Пересчитывает координаты дома в систему отсчёта игрока
            player_coord - коррдинаты игрока, двумерный список/кортеж
            '''
            System_coord = (player_coord[0] - 900, player_coord[1] - 450)
            self.cent = (self.globalx - System_coord[0],\
                self.globaly - System_coord[1])

def proect(coord, spect_coord):
    '''Проецирует точку трехмерную на плоскость двумерную
    coord - трехмерные координаты точки
    spect_coord - трехмерные координаты точки, с которой мы смотрим на объект'''
    xn = coord[0] - spect_coord[0]
    yn = coord[1] - spect_coord[1]
    xn = xn*(spect_coord[2] / (spect_coord[2] - coord[2])) + spect_coord[0]
    yn = yn*(spect_coord[2] / (spect_coord[2] - coord[2])) + spect_coord[1]
    ncoord = (int(xn), int(yn))
    return(ncoord)

'''Дальнейший код написан для тестировки и отладки этого класса, для работы программы в целом -
достаточно просто импортировать отсюда класс домов и функцию проецирования'''

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 700))
house1 = House(screen, 5, 5, 5, (250, 150), (2, 0, 0, 0))
house2 = House(screen, 6, 4, 7, (600, 450), (0, 3, 0, 0))
house3 = House(screen, 3, 4, 3, (300, 450), (0, 0, 3, 0))
finished = False

evx = 0
evy = 0
"""
while not finished:
    screen.fill((255, 255, 255))
    house1.draw((evx, evy, spect))
    house2.draw((evx, evy, spect))
    house3.draw((evx, evy, spect))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                finished = True
        elif event.type == pygame.MOUSEMOTION:
            evx = event.pos[0]
            evy = event.pos[1]
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
"""