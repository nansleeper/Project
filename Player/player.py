import pygame

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
    
    def move(self):
        if ((self.x + self.vx) // 300 >= 3) and ((self.y + self.vy) // 300 >= 2) \
            and ((self.x + self.vx) // 300 <= 44) and ((self.y + self.vy) // 300 <= 29):
            self.x += self.vx
            self.y += self.vy
        self.sector = (self.x // 300, self.y // 300)

    def draw(self, screen):
        v = (self.vx)**2 + (self.vy)**2
        if v == 0:
            player_screen = pygame.image.load('Core/texture/player.bmp')
            player_screen.set_colorkey((255, 255, 255))
            screen.blit(player_screen, (900 - 20, 500 - 16))

        elif v > 0:
            #игрок идёт
            print(1)
        else:
            print('Сворачивай программу, мы в поле комплексных чисел попали!')