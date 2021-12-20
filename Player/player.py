from typing import Any

import pygame
iter = 0

class Player:

    def __init__(self):
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
        self.x = 2800
        self.y = 2800
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
        if ((self.x + self.vx) // 300 >= 3) and ((self.y + self.vy) // 300 >= 2) \
            and ((self.x + self.vx) // 300 <= 44) and ((self.y + self.vy) // 300 <= 29):
            print(self.x,self.y)
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
