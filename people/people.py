import math
import random
import copy as cp
from random import randint, choice

import pygame
import numpy as np
from pygame.draw import *


def point_distance(a, b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5


def vector_sum(a, b):
    return (a[0] + b[0], a[1] + b[1])

class Player:
    def __init__(self, x, y):
        '''
        Класс объектов игрока
        х, у - координаты игрока
        coards - список из этих координта
        car, fire - флаги отвечающие на то, в машине персонаж или нет, стреляет он или нет
        health - здоровье игрока
        sector - список из номеров сектора в котором находится игрок по осям х и у
        vx, vy - скорость по осям
        v - модуль максимальной скорости по осям
        napravl - список из двух элементов указывающий направление
        hitbox - размер хитбокса
        '''
        self.x = x
        self.y = y
        self.coards = [self.x, self.y]
        self.car = False
        self.fire = False
        self.health = 100
        self.sector = (self.x // 300, self.y // 300)
        self.vx = 0
        self.vy = 0
        self.v = 10
        self.napravl = [0.0, 1.0]
        self.hitbox = 10

    def move(self, objects):
        '''
        Функция движения персонажа
        objects - список объектов с которыми он может столкнутся
        '''
        Flag = False
        if ((self.x + self.vx) // 300 >= 3) and ((self.y + self.vy) // 300 >= 2) \
            and ((self.x + self.vx) // 300 <= 44) and ((self.y + self.vy) // 300 <= 29):
            Flag = True
            self.coards = [self.x, self.y]
            for obj in objects:
                if obj.hitbox[0] > abs(obj.cent[0] - 900 - self.vx) - self.hitbox and \
                    obj.hitbox[1] > abs(obj.cent[1] - 500 - self.vy) - self.hitbox:
                        Flag = False
            if Flag == True:
                self.x += self.vx
                self.y += self.vy
        self.sector = (self.x // 300, self.y // 300)
        return Flag

    def move_in_car(self,  car):
        '''
        Функция движения в машине
        car - машина в которой происходит движение
        '''
        if ((int(car.cent[0])) // 300 >= 3) and ((int(car.cent[1])) // 300 >= 2) \
            and ((int(car.cent[0])) // 300 <= 44) and ((int(car.cent[1])) // 300 <= 29):
            Flag = True
          
            if Flag == True:
                self.x = car.cent[0]
                self.y = car.cent[1]
        self.sector = (self.x // 300, self.y // 300)

    def draw(self, screen):
        '''
        Функция отрисовки
        screen - экран на котором идет отрисовка
        '''
        global iter
        v = (self.vx)**2 + (self.vy)**2
        if v == 0:
            if self.car:
                player_screen = pygame.Surface((30, 50))
                player_screen.fill((128, 128, 128))
                self.v = 20
                sh = [15, 25]
            else:
                player_screen = pygame.image.load('Core/texture/player.bmp')
                self.v = 10
                sh = [22, 22]
            player_screen.set_colorkey((0, 0, 0))
            if self.napravl == [0.0, 1.0]:
                screen.blit(player_screen, (900 - sh[0], 500 - sh[1]))
            elif self.napravl == [0.0, -1.0]:
                player_screen = pygame.transform.rotate(player_screen, 180)
                screen.blit(player_screen, (900 - sh[0], 500 - sh[1]))
            elif self.napravl == [1.0, 0.0]:
                player_screen = pygame.transform.rotate(player_screen, 90)
                screen.blit(player_screen, (900 - sh[1], 500 - sh[0]))
            elif self.napravl == [-1.0, 0.0]:
                player_screen = pygame.transform.rotate(player_screen, -90)
                screen.blit(player_screen, (900 - sh[1], 500 - sh[0]))
            elif self.napravl == [1.0, 1.0]:
                player_screen = pygame.transform.rotate(player_screen, 45)
                screen.blit(player_screen, (900 - sh[1], 500 - sh[1]))
            elif self.napravl == [-1.0, 1.0]:
                player_screen = pygame.transform.rotate(player_screen, -45)
                screen.blit(player_screen, (900 - sh[1], 500 - sh[1]))
            elif self.napravl == [-1.0, -1.0]:
                player_screen = pygame.transform.rotate(player_screen, 225)
                screen.blit(player_screen, (900 - sh[1], 500 - sh[1]))
            elif self.napravl == [1.0, -1.0]:
                player_screen = pygame.transform.rotate(player_screen, 135)
                screen.blit(player_screen, (900 - sh[1], 500 - sh[1]))

        elif v > 0:
            iter += 1
            self.napravl[0] = -self.vx / self.v
            self.napravl[1] = -self.vy / self.v
            if iter > 1000 and iter % 2 == 0:
                iter = 0
            if self.car:
                self.v = 20
                sh = [15, 25]
                player_screen = pygame.Surface((30, 50))
                player_screen.fill((128, 128, 128))
            else:
                self.v = 10
                sh = [22, 22]
                if iter % 8 > 3:
                    player_screen = pygame.image.load('Core/texture/player_left.bmp')
                else:
                    player_screen = pygame.image.load('Core/texture/player_right.bmp')
            player_screen.set_colorkey((0, 0, 0))
            if self.napravl == [0.0, 1.0]:
                screen.blit(player_screen, (900 - sh[0], 500 - sh[1]))
            elif self.napravl == [0.0, -1.0]:
                player_screen = pygame.transform.rotate(player_screen, 180)
                screen.blit(player_screen, (900 - sh[0], 500 - sh[1]))
            elif self.napravl == [1.0, 0.0]:
                player_screen = pygame.transform.rotate(player_screen, 90)
                screen.blit(player_screen, (900 - sh[1], 500 - sh[0]))
            elif self.napravl == [-1.0, 0.0]:
                player_screen = pygame.transform.rotate(player_screen, -90)
                screen.blit(player_screen, (900 - sh[1], 500 - sh[0]))
            elif self.napravl == [1.0, 1.0]:
                player_screen = pygame.transform.rotate(player_screen, 45)
                screen.blit(player_screen, (900 - sh[1], 500 - sh[1]))
            elif self.napravl == [-1.0, 1.0]:
                player_screen = pygame.transform.rotate(player_screen, -45)
                screen.blit(player_screen, (900 - sh[1], 500 - sh[1]))
            elif self.napravl == [-1.0, -1.0]:
                player_screen = pygame.transform.rotate(player_screen, 225)
                screen.blit(player_screen, (900 - sh[1], 500 - sh[1]))
            elif self.napravl == [1.0, -1.0]:
                player_screen = pygame.transform.rotate(player_screen, 135)
                screen.blit(player_screen, (900 - sh[1], 500 - sh[1]))
        else:
            print('Сворачивай программу, мы в поле комплексных чисел попали!')
class Human:
    min_fahm = 10 ** 18
    def __init__(self, x, y, r=100):
        self.inner = Player(x, y);
        r = 14
        step = 0
        Human.min_fahm -= 1
        self.is_stoopid = False
        self.fahm = Human.min_fahm
        self.steps_done = 0
        self.coords = (x, y)
        self.velocity = (0, 0)
        min_velocity = 3.
        while self.velocity[0] * self.velocity[0] + self.velocity[1] + self.velocity[1] < min_velocity * min_velocity:
            self.velocity = np.random.randint(-4 * min_velocity, 4 * min_velocity, size=(2)).astype(float)
        self.velocity = (self.velocity[0], self.velocity[1])

        self.orientation = np.angle([self.velocity[0]+self.velocity[1]*1j], deg=True)
        self.wished_orientation = self.orientation

        if type(r) in (tuple, list, np.array):
            self.r = random.uniform(r[0], r[1])
        else:
            self.r = r

        self.surface = pygame.Surface((2 * self.r, 2 * self.r), pygame.SRCALPHA)
        self.surface.set_colorkey((255, 255, 255))
        self.rect = self.surface.get_rect(center=(x, y))

        self.is_alive = True


    def move(self, dt, people, Map_activesectors):
        is_active = False
        for sector in Map_activesectors:
            if self.collides2(sector.globalcent, 300):
                is_active = True
            if abs(self.coords[1] - sector.globalcent[1]) > 1300 or point_distance(self.coords, sector.globalcent) > 2000:
                is_alive = False
                return
        #if not is_active:
            #self.is_alive = False
            #return


        
        rotation = 10
        self.orientation = self.wished_orientation
        for attempts in range(360 // rotation + 1):
            if self.inner.move(Map_activesectors):
                self.is_stoopid = False
                self.steps_done += 1
                #self.step += 1
                self.coords = (self.inner.x, self.inner.y) #cp.deepcopy(copy.coords)
            #class Dzu:
            #    pass
            #copy = Dzu()
            #copy.coords = cp.deepcopy(self.coords)
            #copy.r = cp.deepcopy(self.r)
            #copy.coords = vector_sum(copy.coords, self.velocity * dt)
            #canMove = True
            #for idiot in people:
            #    if idiot != self and idiot.is_alive and idiot.collides1(copy):
            #        if self.fahm < idiot.fahm:
            #            return
            #        #print(idiot.coords, ' ', copy.coords)
            #        canMove = False
            #for sector in Map_activesectors:
            #    if str(sector) in ['House'] and \
            #    self.collides2(sector.globalcent, 170): # How long is the side of a house?
            #        canMove = False
            #        self.wished_orientation = self.orientation
            #for sector in Map_activesectors:
            #    if str(sector) in ['Cross', 'Hor', 'Vert', \
            #    'Border', 'Water', 'Bridge'] and \
            #    self.collides2(sector.globalcent, 305):
            #        canMove = False
            #        self.wished_orientation = self.orientation
                    #canMove = True
                    #self.orientation += 90
                    #self.orientation %= 360
                    #self.wished_orientation = self.orientation
            #if canMove == True:
            #    self.is_stoopid = False
            #    self.steps_done += 1
            #    self.step += 1
            #    self.coords = cp.deepcopy(copy.coords)
            #    return
        #        # print("Rotating...")
            self.orientation += rotation
            self.velocity = (self.velocity[0] * math.cos(self.orientation) - self.velocity[1] * math.sin(self.orientation),
                             self.velocity[0] * math.sin(self.orientation) + self.velocity[1] * math.cos(self.orientation))
        #print('lavn el qunem')
        #print(self.coords)
        #for sector in Map_activesectors:
        #    if str(sector) in ['Cross', 'Hor', 'Vert', \
        #    'Border', 'Water', 'Bridge']:
        #        print(sector.globalcent)
        #self.is_stoopid = True
        #Human.min_fahm -= 1
        #fahm = Human.min_fahm


    def collides1(self, rhs):
        distance = ((self.coords[0] - rhs.coords[0]) ** 2 + (self.coords[1] - rhs.coords[1]) ** 2) ** 0.5
        return distance < 1 + 1 #self.r + rhs.r


    def collides2(self, center, side):
        for c in (0, 1):
            for border in (center[c] - side / 2, center[c] + side / 2):
                if abs(self.coords[c] - border) < 1:#self.r:

                    return True
        for vertex in ((center[c] - side / 2, center[c] - side / 2), \
                       (center[c] - side / 2, center[c] + side / 2), \
                       (center[c] + side / 2, center[c] - side / 2), \
                       (center[c] + side / 2, center[c] + side / 2)):

            if point_distance(self.coords, vertex) < 1:#self.r:

                return True
        if center[0] - side / 2 <= self.coords[0] and self.coords[0] <= center[0] + side / 2:
            if center[1] - side / 2 <= self.coords[1] and self.coords[1] <= center[1] + side / 2:
                return True
        return False


    def render(self, display, Map_activesectors):
        surface=self.surface
        if self.is_alive:
            roja = './people/chuvak'
            if self.is_stoopid:
                roja += '1'
            else:
                roja += str((self.steps_done) % 15 + 1)
            roja += '.png'
            #roja = 'people/koldunov.jpg'
            e, st = 0, 0
            if len(Map_activesectors) > 0:
                e = cp.deepcopy(Map_activesectors[0].cent)
                st = cp.deepcopy(Map_activesectors[0].globalcent)
            else:
                e = (0, 0)
                st = (0, 0)
            e = (e[0], e[1])
            st = (-st[0], -st[1])
            to_screen = vector_sum(st, e)
            koldunov = pygame.image.load(roja)
            koldunov.set_colorkey((0,0,0))
            koldunov = koldunov.convert_alpha()
            correct_scale = 2 * self.r
            orientation = np.angle([self.velocity[0]+self.velocity[1]*1j], deg=True)
            correct_scale *= (abs(math.sin(orientation)) +
                              abs(math.cos(orientation)))
            correct_scale = math.ceil(2 * self.r / correct_scale)
            correct_scale = math.ceil(2 * self.r)
            koldunov = pygame.transform.scale(koldunov, (correct_scale, correct_scale));
            koldunov = pygame.transform.rotate(koldunov, self.orientation);
            display.blit(koldunov, (self.coords[0] - self.r + to_screen[0], self.coords[1] - self.r + to_screen[1]))


def birth(people, x, y):
    # Don't overpopulate the mini-city.
    if len(people) > 20:
        return people
    people.append(Human(x, y, (30, 40)))
    return people


def init_people(people):
    zibil = 5
    for i in range(zibil):
        for j in range(zibil):
            people = birth(people, (i + 1) * 800 / (zibil + 1), (j + 1) * 800 / (zibil + 1))
    return people


def move_people(people, Map_activesectors):
    for idiot in people:
        idiot.move(1, people, Map_activesectors)


def tick(display, people, Map_activesectors):
    for idiot in people:
        if idiot.is_alive:
            idiot.move(1, people, Map_activesectors)
            idiot.render(display, Map_activesectors)
    living_people = []
    for idiot in people:
        if idiot.is_alive:
            living_people.append(idiot)
    people = living_people
    return people

#if __name__ == '__main__':
def run_randomly_eat_stuff(Map_activesectors):
    pygame.init()

    FPS = 5
    SIDES = [1690, 690]

    display = pygame.display.set_mode(SIDES)

    pygame.display.update()
    clock = pygame.time.Clock()
    gameover = False

    pygame.init()
    people = []
    people = init_people(people)
    SCREEN = (WIDTH, HEIGHT) = (1200, 800)
    win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)

    while True:
        pygame.display.update()
        clock = pygame.time.Clock()
        clock.tick(FPS)
        display.fill((0, 0, 0))
        people = tick(display, people, Map_activesectors)
        pygame.display.update()

#run_randomly_eat_stuff([])
