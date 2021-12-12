import pygame
from pygame.constants import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, K_d, K_KP_ENTER



class Menu:

    def __init__(self, screen):
        self.but_num = 2
        self.but_now = -1
        self.pos = [0, 0]
        self.m_push = 0
        self.screen = screen
        self.menu_y = 300
        self.start_num = 0
        self.width = 100
        self.length = 600
        self.start_y = self.menu_y + self.width * self.start_num
        self.exit_num = 1
        self.exit_y = self.menu_y + self.width * self.exit_num
        self.status = True
        self.finished = False
        self.time = 0
        self.period = 500

    def start(self):
        self.status = False
    
    def start_draw(self, gamestatus):
        if self.but_now == 0:
            pygame.draw.rect(self.screen, (50, 50, 50), (30, self.start_y, self.length, self.width))
        fontstart = pygame.font.Font(None, 60)
        if gamestatus == 'new':
            start_text = fontstart.render('Start new game', True, (255, 255, 255))
        else:
            start_text = fontstart.render('Continue game', True, (255, 255, 255))
        self.screen.blit(start_text, (100, self.start_y + self.width / 2))

    def exit(self):
        self.status = False
        self.finished = True

    def exit_draw(self):
        if self.but_now == 1:
            pygame.draw.rect(self.screen, (50, 50, 50), (30, self.exit_y, self.length, self.width))
        fontstart = pygame.font.Font(None, 60)
        start_text = fontstart.render('Exit', True, (255, 255, 255))
        self.screen.blit(start_text, (100, self.exit_y + self.width / 2))
    '''
    def draw_pict(self):
        if self.time % self.period < self.period // 3:
            pict_path = 'Menu/pictures/pict1.bmp'
        elif self.time % self.period < 2 * self.period // 3:
            pict_path = 'Menu/pictures/pict2.bmp'
        else:
            pict_path = 'Menu/pictures/pict3.bmp'
        image = pygame.image.load(pict_path)
        image = pygame.transform.scale(image, (int(700 - 650 * ((self.time % (self.period / 3) / (self.period / 3)))),\
             int(700 - 650 * (self.time % (self.period / 3) / (self.period / 3)))))
        image = pygame.transform.scale(image, (700, 700))
        self.screen.blit(image, (900, 150))
    '''
        
    def draw_background(self):
        backspace = pygame.image.load('Menu/pictures/backspace.bmp')
        backspace = pygame.transform.scale(backspace, (1800, 1000))
        self.screen.blit(backspace, (0, 0))


        

    def draw(self, gamestatus):
        
        self.calculate()
        self.draw_background()
        pygame.draw.polygon(self.screen, (0, 0, 0), ((0,0), (600, 0), (800, 1000), (0, 1000)))
        self.start_draw(gamestatus)
        self.exit_draw()
        self.time += 1
        

    def calculate(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.but_now / 1 == 0:
                    self.start()
                elif self.but_now / 1 == 1:
                    self.exit()
            elif event.type == pygame.MOUSEMOTION:
                self.pos = event.pos
                self.but_now = (self.pos[1] - self.menu_y) // 100
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    if self.status:
                        self.status = False
                    else:
                        self.status = True
                elif event.key == 13:  # actually it is Enter
                    if self.but_now == 0:
                        self.start()
                    elif self.but_now == 1:
                        self.exit()
                elif event.key == K_UP:
                    if self.but_now > 0 and self.but_now < self.but_num:
                        self.but_now -= 1
                    elif self.but_now <= 0 or self.but_num >= self.but_num:
                        self.but_now = self.but_num - 1
                elif event.key == K_DOWN:
                    if self.but_now >= 0 and self.but_now < self.but_num - 1:
                        self.but_now += 1
                    elif self.but_now < 0 or self.but_num >= self.but_num - 1:
                        self.but_now = 0

