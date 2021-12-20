import math
import pygame
from pygame.draw import *

class Car():
    '''
    Класс машин, реализует движение неуправляемых и управляемых машин машин
    '''
    def __init__(self, win, globalcent, angle):
        '''
        win - поверхность, на которой отрисовывается машина, globalcent - глобальные координаты для машины,
        angle - первоначальный угол поворота машины, отсчитывается против часовой стрелки, 0 соответсвует вертикальное положение
        self.v - скорость машины, self.avast - остановка машины, self.hit - проверка на столкновение, self.playerstatus - проверка на присутствие человека в машине,
        self.unable - определяет брошенную машину, self.sector - определяет сектор нахождения машины,self.t_unable - время после того, как машину бросили ,  
        self.rotate - определяет поворот при столкновении, self.n - параметр для направления движения, self.start - определяе старт для управляемой машины,
        self.t - вреемф после солкновения, self.color - цвет машины, self.not_colid - проверка на столкновение, self.first_collid - первое столкновение,
        self.motion0 - последнее направление перед столкновением,
        self.angle_colid - угол столкновения, self.after_col - направление после столкновения, self.side1 - одна сторона машины, self.side2 - вторая сторона машины 
        '''
        self.globalcent = globalcent
        self.win = win
        self.cent = [0, 0]
        self.v = 5
        self.dv = ()
        self.angle = angle 
        self.avast = False
        self.hit = False
        self.playerstatus = False
        self.unable = False
        self.sector = [int(globalcent[0] // 300), int(globalcent[1] // 300)]
        self.t_unable = 0
        self.rotate = False 
        self.n = 2 
        self.start = 0
        self.t = 0
        self.color = (128, 128, 128)
        self.not_colid = True
        self.first_collid = False
        self.motion0 = []
        self.angle_col = 0
        self.after_collid = 0
        self.side1 = 30
        self.side2 = 50

        '''
        Задаётся маленькая поверхность, внутри которой помещён прямоугольник
        '''
        self.surface = pygame.Surface((self.side1, self.side2), pygame.SRCALPHA,32)
        self.surface.set_colorkey((255,255,255, 0))
        self.rect = self.surface.get_rect(center=(self.globalcent[0], self.globalcent[1]))

    def collisions(self, obj):
        '''
        проверка на столкноввение двух машин
        '''
        if self.rect.colliderect(obj.rect):
          self.hit = True

    def stop(self, obj, MAP_Sector):
        '''
        проверяет есть ли машина перед ней на определенном расстоянии interval, 
        если есть - self.avast = True
        '''

        if self.playerstatus == False:
            if self.angle == 0 or self.angle == 180:
                if abs(self.y - obj.y) <= 3/2 * self.side2:
                    self.avast = True

            if self.angle == 90 or self.angle == 270:
                if abs(self.x - obj.x) <= 3/2 * self.side2:
                    self.avast = True

        self.t_unbale += 1

        if MAP_Sector == "cross":
            if abs(MAP_Sector.angle - self.angle) > 45 and self.rotate == False:
                self.avast = True


    def move(self, player, dv = [0, 0, 0, 0], playerstatus = False):
        '''
        функция задающая движение и отрисовку
        dv = (0 w, 0 a, 0 s, 0 d) - передаёт события с клавиатуры
        player - несёт в себе информацию о положении центра, нужен для пересчитывания координат
        '''
        self.playerstatus = playerstatus
        self.dv = dv
        center = (player.coards[0], player.coards[1])
        if not (self.playerstatus):
          if self.avast and self.t < 1:
            '''
            Функция для остановки неуправляемых машин
            '''

            center = self.rect.center
            image = pygame.transform.rotate(self.surface, -self.angle)
            self.rect = image.get_rect()
            self.rect.center = center
            pygame.draw.rect(self.surface, self.color, (0,0, self.side1, self.side2))
            self.win.blit(image, self.rect)

            self.t += 0.005

            self.cent[0] = self.globalcent[0] - player.coards[0] + 900
            self.cent[1] = self.globalcent[1] - player.coards[1] + 500

            self.sector = [int(self.globalcent[0] // 300), int(self.globalcent[1] // 300)]

          else:
            '''
            функция движения неуправляемых машин
            '''
  
            image = pygame.transform.rotate(self.surface, self.angle)
            self.rect = image.get_rect()
            center = self.rect.center
            self.globalcent[0] += self.v * math.sin(math.radians(self.angle))
            self.globalcent[1] += self.v * math.cos(math.radians(self.angle))

            self.rect.x = self.globalcent[0] - player.coards[0] + 900
            self.rect.y = self.globalcent[1] - player.coards[1] + 500

            center = self.rect.center
            '''
            Отрисовка
            '''
            pygame.draw.rect(self.surface, self.color, (0,0, self.side1, self.side2))
            self.win.blit(image, self.rect)
            '''
            перевод глобальных координат в локальные
            '''
            self.cent[0] = self.globalcent[0] - player.coards[0] + 900
            self.cent[1] = self.globalcent[1] - player.coards[1] + 500

            self.sector = [int(self.globalcent[0] // 300), int(self.globalcent[1] // 300)]
            
        elif self.unable:
            '''
            функция для брошенной машины
            '''
            self.t_unable += 1

            center = self.rect.center
            image = pygame.transform.rotate(self.surface, -self.angle)
            self.rect = image.get_rect()
            self.rect.center = center
            pygame.draw.rect(self.surface, self.color, (0,0, self.side1, self.side2))

            self.cent[0] = self.globalcent[0] - player.coards[0] + 900
            self.cent[1] = self.globalcent[1] - player.coards[1] + 500

            self.win.blit(image, self.rect)

            self.sector = [int(self.globalcent[0] // 300), int(self.globalcent[1] // 300)]




        if self.playerstatus == True:
            '''
            человек управляет машиной с помощью клавиатуры
            '''
            if self.hit and self.t >= 1:

              self.t = 0
              self.v = 0
              self.not_colid = False
            if self.not_colid == False:
              self.after_collid = 0
              self.col_update()
            if self.not_colid == True:

              if self.after_collid == 1 and (self.dv == self.motion0 or (self.dv[0] == self.motion0[0] or self.dv[2] == self.motion0[2])):
                  self.t = 0
                  self.vx = 0
                  self.vy = 0
                  self.col_update()
                  self.not_colid = False
              
              else:
                  
                  if self.dv[0] != 0 and (self.dv[1] != 0 or self.dv[3] != 0):
                      if self.dv[1] != 0:
                        self.n = 1

                      center = self.rect.center
                      self.angle = (self.angle - ((-1)**n) * self.v/2) % 360

                  if self.dv[2] != 0 and (self.dv[1] != 0 or self.dv[3] != 0):
                      if self.dv[1] != 0:
                          self.n = 1

                      center = self.rect.center
                      self.angle = (self.angle + ((-1)**n) * self.v/2) % 360
                  '''
                  Поворачивает прямоугольник
                  '''
                  image = pygame.transform.rotate(self.surface, self.angle)
                  self.rect = image.get_rect()
                  self.rect.center = center

                  if self.dv[0] != 0:

                    player.y -= self.v * math.cos(math.radians(360-self.angle))
                    player.x += self.v * math.sin(math.radians(360-self.angle))
                    self.rect.y = player.y
                    self.rect.x = player.x
                    if self.start > 0:
                      self.rect.center = (self.rect.x - int(pygame.Surface.get_width(self.surface)/2), self.rect.y - int(pygame.Surface.get_height(self.surface)/2))
                    if self.start == 0:
                      self.start = 1
                      self.rect.center = (self.rect.x - int(pygame.Surface.get_width(self.surface)/2), self.rect.y - int(pygame.Surface.get_height(self.surface)/2))

                  if self.dv[2] != 0 :

                    player.y += self.v * math.cos(math.radians(360-self.angle))
                    player.x -= self.v * math.sin(math.radians(360-self.angle))
                    self.rect.y = player.y
                    self.rect.x = player.x
                    if self.start > 0:
                      self.rect.center = (self.rect.x - int(pygame.Surface.get_width(self.surface)/2), self.rect.y - int(pygame.Surface.get_height(self.surface)/2))
                    if self.start == 0:
                      self.start = 1
                      self.rect.center = (self.rect.x - int(pygame.Surface.get_width(self.surface)/2), self.rect.y - int(pygame.Surface.get_height(self.surface)/2))

                  self.after_collid = 0

                  if not 0 in dv:
                      self.motion0 = dv
                      center = self.rect.center
                  '''
                  отрисовка машинки
                  '''
                  self.cent[0] = player.x
                  self.cent[1] = player.y
                  pygame.draw.rect(self.surface, self.color, (0, 0, self.side1, self.side2))
                  self.win.blit(image, self.rect)
                  self.sector = [int(player.coards[0] // 300), int(player.coards[1] // 300)]


    def col_update(self):
      '''
      задаёт движение машины после столкновения
      '''

      self.t += self.dt
      
      if self.v <= 5:
        self.v += 2
        
      image = pygame.transform.rotate(self.surface, self.angle)
      self.rect = image.get_rect()

      self.rect.x = player.coards[0]
      self.rect.y = player.coards[1]
      
      self.rect.center = (self.rect.x - int(pygame.Surface.get_width(self.surface)/2), self.rect.y - int(pygame.Surface.get_height(self.surface)/2))

      pygame.draw.rect(self.surface, self.color, (0,0, self.side1, self.side2))
      self.win.blit(image, self.rect)

      if self.t >= 1:
        self.not_colid = True
        self.hit = False
        self.after_collid = 1

    def man_in_car(self, player):
        '''
        проверяет наличие человека в машине
        '''
        if (abs(player.coards[0] - self.globalcent[0]) <= self.side2 + 5) and (abs(player.coards[1] - self.globalcent[1]) <= self.side2 + 5):
            return True

        else:
            return False
