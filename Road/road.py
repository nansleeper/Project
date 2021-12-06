import pygame

class Road:

    def __init__(self, screen, cent):

        'orientation - vert, hor or cross'

        self.screen = screen
        self.globalx = cent[0]
        self.globaly = cent[1]
        self.cent = cent
        self.sector =(self.globalx // 300, self.globaly // 300)
        if self.sector[0] % 5 == 0 and self.sector[1] % 5 == 0:
            self.tex = 'textur/cross.bmp'
        else:
            if self.sector[0] % 5 == 0:
                self.tex = 'textur/vert.bmp'
            else:
                self.tex = 'textur/hor.bmp'

    def move(self, player_coord):
            '''
            Пересчитывает координаты дома в систему отсчёта игрока
            player_coord - коррдинаты игрока, двумерный список/кортеж
            '''
            System_coord = (player_coord[0] - 900, player_coord[1] - 450)
            self.cent = (self.globalx - System_coord[0],\
                self.globaly - System_coord[1])

    def draw(self):
        tex = pygame.image.load(self.tex)
        self.screen.blit(tex, (self.cent[0] - 150, self.cent[1] - 150))
        
