from typing import Any

import pygame
iter = 0

class Player:

    def __init__(self):
        self.x = 1800
        self.y = 1800
        self.car = False
        self.fire = False
        self.health = 100
        self.sector = (self.x // 300, self.y // 300)
        self.vx = 0
        self.vy = 0
        self.napravl = [0.0, 1.0]
        self.hitbox = 10

    def move(self, objects):
        if ((self.x + self.vx) // 300 >= 3) and ((self.y + self.vy) // 300 >= 2) \
            and ((self.x + self.vx) // 300 <= 44) and ((self.y + self.vy) // 300 <= 29):
            Flag = True
            for obj in objects:
                if obj.hitbox[0] > abs(obj.cent[0] - 900 - self.vx) - self.hitbox and \
                    obj.hitbox[1] > abs(obj.cent[1] - 500 - self.vy) - self.hitbox:
                        Flag = False
            if Flag == True:
                self.x += self.vx
                self.y += self.vy
        self.sector = (self.x // 300, self.y // 300)

    def draw(self, screen):
        global iter
        v = (self.vx)**2 + (self.vy)**2
        if v == 0:
            player_screen = pygame.image.load('Core/texture/player.bmp')
            player_screen.set_colorkey((0, 0, 0))
            if self.napravl == [0.0, 1.0]:
                screen.blit(player_screen, (900 - 20, 500 - 16))
            elif self.napravl == [0.0, -1.0]:
                player_screen = pygame.transform.rotate(player_screen, 180)
                screen.blit(player_screen, (900 - 20, 500 - 16))
            elif self.napravl == [1.0, 0.0]:
                player_screen = pygame.transform.rotate(player_screen, 90)
                screen.blit(player_screen, (900 - 20, 500 - 16))
            elif self.napravl == [-1.0, 0.0]:
                player_screen = pygame.transform.rotate(player_screen, -90)
                screen.blit(player_screen, (900 - 20, 500 - 16))
            elif self.napravl == [1.0, 1.0]:
                player_screen = pygame.transform.rotate(player_screen, 45)
                screen.blit(player_screen, (900 - 20, 500 - 16))
            elif self.napravl == [-1.0, 1.0]:
                player_screen = pygame.transform.rotate(player_screen, -45)
                screen.blit(player_screen, (900 - 20, 500 - 16))
            elif self.napravl == [-1.0, -1.0]:
                player_screen = pygame.transform.rotate(player_screen, 225)
                screen.blit(player_screen, (900 - 20, 500 - 16))
            elif self.napravl == [1.0, -1.0]:
                player_screen = pygame.transform.rotate(player_screen, 135)
                screen.blit(player_screen, (900 - 20, 500 - 16))

        elif v > 0:
            iter += 1
            self.napravl[0] = -self.vx / 10
            self.napravl[1] = -self.vy / 10
            if iter > 1000 and iter % 2 == 0:
                iter = 0
            if iter % 8 > 3:
                player_screen = pygame.image.load('Core/texture/player_left.bmp')
            else:
                player_screen = pygame.image.load('Core/texture/player_right.bmp')
            player_screen.set_colorkey((0, 0, 0))
            if self.napravl == [0.0, 1.0]:
                screen.blit(player_screen, (900 - 21, 500 - 15))
            elif self.napravl == [0.0, -1.0]:
                player_screen = pygame.transform.rotate(player_screen, 180)
                screen.blit(player_screen, (900 - 21, 500 - 15))
            elif self.napravl == [1.0, 0.0]:
                player_screen = pygame.transform.rotate(player_screen, 90)
                screen.blit(player_screen, (900 - 21, 500 - 15))
            elif self.napravl == [-1.0, 0.0]:
                player_screen = pygame.transform.rotate(player_screen, -90)
                screen.blit(player_screen, (900 - 21, 500 - 15))
            elif self.napravl == [1.0, 1.0]:
                player_screen = pygame.transform.rotate(player_screen, 45)
                screen.blit(player_screen, (900 - 21, 500 - 15))
            elif self.napravl == [-1.0, 1.0]:
                player_screen = pygame.transform.rotate(player_screen, -45)
                screen.blit(player_screen, (900 - 21, 500 - 15))
            elif self.napravl == [-1.0, -1.0]:
                player_screen = pygame.transform.rotate(player_screen, 225)
                screen.blit(player_screen, (900 - 21, 500 - 15))
            elif self.napravl == [1.0, -1.0]:
                player_screen = pygame.transform.rotate(player_screen, 135)
                screen.blit(player_screen, (900 - 21, 500 - 15))
        else:
            print('Сворачивай программу, мы в поле комплексных чисел попали!')