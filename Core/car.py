import math
import pygame
from pygame.draw import *

class Car():
    def __init__(self, win, globalcent, angle, playerstatus = False):
        self.globalcent = [globalcent[0], globalcent[1]]
        self.win = win
        self.cent = [0, 0]
        self.v = 5
        self.direction_v = []
        self.dv = ()
        self.angle = angle 
        self.stop = False
        self.hit = False
        self.playerstatus = playerstatus
        self.unable = False
        self.sector = [globalcent[0] // 300, globalcent[1] // 300]
        #self.tex = textur
        self.t_unable = 0
        self.rotate = False 
        self.traectory = [0, 0, 0]
        self.n = 2 
        self.start = 0
        self.t = 0
        self.color = (0, 0, 0)

        self.not_colid = True
        self.first_collid = False
        self.motion0 = []
        self.angle_col = 0
        self.after_collid = 0

        self.side1 = 30
        self.side2 = 50

        self.surface = pygame.Surface((self.side1, self.side2), pygame.SRCALPHA,32)
        self.surface.set_colorkey((255,255,255, 0))
        self.rect = self.surface.get_rect(center=(self.globalcent[0], self.globalcent[1]))

    def collisions(self, obj):
        if self.rect.colliderect(obj.rect):
          self.hit = True

    def stop(self, obj, MAP_Sector):
        '''
        проверяет есть ли машина перед ней на определенном расстоянии interval 
        если есть - self.stop = True
        '''

        if self.playerstatus == False:
            if self.angle == 0 or self.angle == 180:
                if abs(self.y - obj.y) <= 3/2 * self.side2:
                    self.stop = True

            if self.angle == 90 or self.angle == 270:
                if abs(self.x - obj.x) <= 3/2 * self.side2:
                    self.stop = True

        self.t_unbale += 1

        if MAP_Sector == "cross":
            if abs(MAP_Sector.angle - self.angle) > 45 and self.rotate == False:
                self.stop = True


    def move(self, player = False, dv = [0, 0, 0, 0]):
        '''
        dv = (0 w, 0 a, 0 s, 0 d)
        '''
        self.dv = dv
        if not (self.playerstatus):
          if self.stop and self.t < 1:

            center = self.rect.center
            image = pygame.transform.rotate(self.surface, -self.angle)
            self.rect = image.get_rect()
            self.rect.center = center
            pygame.draw.rect(self.surface, self.color, (0,0, self.side1, self.side2))
            self.win.blit(image, self.rect)

            self.t += 0.005

            self.cent[0] = self.globalcent[0] - player.coards[0] + 900
            self.cent[1] = self.globalcent[1] - player.coards[1] + 500

          else:
            if abs(self.traectory[0] - self.globalcent[0]) != 0:
              self.direction_v.append((self.traectory[0] - self.globalcent[0]) / abs(self.traectory[0] - self.globalcent[0]))
            else:
              self.direction_v.append(0)
            if abs(self.traectory[1] - self.globalcent[1]) != 0:
              self.direction_v.append((self.traectory[1] - self.globalcent[1]) / abs(self.traectory[1] - self.globalcent[1]))
            else:
              self.direction_v.append(0)
            if abs(self.traectory[2] - self.angle) != 0:
              self.direction_v.append((self.traectory[2] - self.angle) / abs(self.traectory[2] - self.angle))
            else:
              self.direction_v.append(0)

            if abs(self.traectory[2] - self.angle) <= 180:
                self.angle = (self.angle - self.direction_v[2] * self.v/2) % 360

            else:
                self.angle = (self.angle + self.direction_v[2] * self.v/2) % 360

            image = pygame.transform.rotate(self.surface, self.angle)
            self.rect = image.get_rect()
            center = self.rect.center

            self.globalcent[0] += self.v * self.direction_v[0] * abs(math.sin(self.angle))
            self.globalcent[1] += self.v * self.direction_v[1] * abs(math.cos(self.angle))

            self.rect.x = self.globalcent[0]
            self.rect.y = self.globalcent[1]

            center = self.rect.center

            pygame.draw.rect(self.surface, self.color, (0,0, self.side1, self.side2))
            self.win.blit(image, self.rect)

            self.direction_v.clear()

            self.cent[0] = self.globalcent[0] - player.coards[0] + 900
            self.cent[1] = self.globalcent[1] - player.coards[1] + 500
            

            '''
            траектори - к этому положения устремить машину


            '''
        elif self.unable:
            self.t_unable += 1

            center = self.rect.center
            image = pygame.transform.rotate(self.surface, -self.angle)
            self.rect = image.get_rect()
            self.rect.center = center
            pygame.draw.rect(self.surface, self.color, (0,0, self.side1, self.side2))

            self.cent[0] = self.globalcent[0] - player.coards[0] + 900
            self.cent[1] = self.globalcent[1] - player.coards[1] + 500

            self.win.blit(image, self.rect)




        else:
            '''
            человек управляет машиной с помощью dv (второстепенная задача)
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

                self.globalcent[1] -= self.v * math.cos(math.radians(360-self.angle))
                self.globalcent[0] += self.v * math.sin(math.radians(360-self.angle))
                self.rect.y = self.globalcent[1]
                self.rect.x = self.globalcent[0]
                if self.start > 0:
                  self.rect.center = (self.rect.x - int(pygame.Surface.get_width(self.surface)/2), self.rect.y - int(pygame.Surface.get_height(self.surface)/2))
                if self.start == 0:
                  self.start = 1
                  self.rect.center = (self.rect.x - int(pygame.Surface.get_width(self.surface)/2), self.rect.y - int(pygame.Surface.get_height(self.surface)/2))

              if self.dv[2] != 0 :

                self.globalcent[1] += self.v * math.cos(math.radians(360-self.angle))
                self.globalcent[0] -= self.v * math.sin(math.radians(360-self.angle))
                self.rect.y = self.globalcent[1]
                self.rect.x = self.globalcent[0]
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
              self.cent[0] = self.globalcent[0] - player.coards[0] + 900
              self.cent[1] = self.globalcent[1] - player.coards[1] + 500
              pygame.draw.rect(self.surface, self.color, (0, 0, self.side1, self.side2))
              self.win.blit(image, self.rect)

    def col_update(self):

      self.t += self.dt
      print(self.t)
      
      if self.v <= 5:
        self.v += 2
        
      image = pygame.transform.rotate(self.surface, self.angle)
      self.rect = image.get_rect()

      self.rect.x = self.globalcent[0]
      self.rect.y = self.globalcent[1]
      
      self.rect.center = (self.rect.x - int(pygame.Surface.get_width(self.surface)/2), self.rect.y - int(pygame.Surface.get_height(self.surface)/2))

      pygame.draw.rect(self.surface, self.color, (0,0, self.side1, self.side2))
      self.win.blit(image, self.rect)

      if self.t >= 1:
        self.not_colid = True
        self.hit = False
        self.after_collid = 1
