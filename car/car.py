
import math
import pygame
import random
from random import choice
from pygame.draw import *
from random import randint

FPS = 5
height = 800
width = 1000
score = 0
i = 0
n = 2
motion = 0
cars = []
car1 = []


coord_gor = [0, width]

GREY = (77, 77, 77)
BLACK = (0, 0, 0)
WHIGHT = (255, 255, 255)
GREEN = (204, 255, 102)
PINK = (255, 102, 255)
COLOR = [GREEN, PINK]

screen = pygame.display.set_mode((width, height))
screen.fill(WHIGHT)


class Road:
  def __init__(self, x, y):
    self.r_width = 100
    self.x = x
    self.y = y
    if self.x > 0:
      self.center1 = self.x + self.r_width/4 
      self.center2 = self.x + self.r_width*3/4
    else:
      self.center1 = self.y + self.r_width/4
      self.center2 = self.y + self.r_width*3/4

  def parametrs():
    return self.x, self.y, self.r_width

  def drawing(self, win):
    
    if self.x > 0:
      pygame.draw.polygon(win, GREY, [(self.x, self.y), (self.x + self.r_width, self.y),
                               (self.x + self.r_width, height), (self.x, height)])

    if self.y > 0:
      pygame.draw.polygon(win, GREY, [(self.x, self.y), (width, self.y),
                               (width, self.y + self.r_width), (self.x, self.y + self.r_width)])

class Square(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Square, self).__init__()

        self.win = win
        self.color = (128, 128, 128)
        self.speed = 3
        self.angle = 0
        self.hit = 0
        self.t = 0 
        self.n = 0

        self.side1 = 30
        self.side2 = 50

        self.surface = pygame.Surface((self.side1, self.side2), pygame.SRCALPHA,32)
        self.surface.set_colorkey((255,255,255, 0))
        self.rect = self.surface.get_rect(center=(x, y))


    def update(self, win, n, orientation = 2, angle = 0, parametr = width):
      '''orientation- 1 горизонтально, 2 вертикально'''
      self.n = n
      if self.hit == 1 and self.t < 1:

        center = self.rect.center
        image = pygame.transform.rotate(self.surface, -self.angle)
        self.rect = image.get_rect()
        self.rect.center = center
        pygame.draw.rect(self.surface, self.color, (0,0, self.side1, self.side2))
        win.blit(image, self.rect)

        self.t += 0.01

      else:

        self.angle = angle 
        center = self.rect.center
        if center[1] - self.side2/2 >= parametr and self.angle < 90 and n == 2:
          self.angle = (self.angle + self.speed) % 360
          #self.rect.x, self.rect.y = self.rect.y, self.rect.x
          
        image = pygame.transform.rotate(self.surface, self.angle)
        self.rect = image.get_rect()
        self.rect.center = center

        if self.angle == 90 or orientation == 1:
          self.rect.x += 1.5 * (-1)**n
         
        else:
          self.rect.y += 1.5 * (-1)**n

        if self.rect.top >= HEIGHT:
          self.kill()

        pygame.draw.rect(self.surface, self.color, (0,0, self.side1, self.side2))
        win.blit(image, self.rect)

      


      '''else:
        center = self.rect.center
        image = pygame.transform.rotate(self.surface, self.angle)
        self.rect = image.get_rect()
        self.rect.center = center
        pygame.draw.rect(self.surface, self.color, (0,0, self.side1, self.side2))
        win.blit(image, self.rect)'''



    def collisions(self, obj):
      center = self.rect.center
      self.hit = 1
      self.t = 0
      '''
      if self.rect.x > obj.x:
        self.angle = (self.angle + self.speed) % 360
      '''
      image = pygame.transform.rotate(self.surface, self.angle)
      self.rect = image.get_rect()
      self.rect.center = center

      '''
      self.rect.x += (self.rect.x - obj.x)/abs(self.rect.x - obj.x) * 20 * math.sin(math.radians(360-self.angle)) * (-1)**n
      self.rect.y -= (self.rect.y - obj.y)/abs(self.rect.y - obj.y) * 20 * math.cos(math.radians(360-self.angle)) * (-1)**n
      '''
      pygame.draw.rect(self.surface, self.color, (0,0, self.side1, self.side2))
      win.blit(image, self.rect)



class Square_main(Square):
  def __init__(self, x, y):
    super().__init__(x, y)
    self.x = self.rect.x
    self.y = self.rect.y
    self.start = 0
    self.vx = 5
    self.vy = 5
    self.a = 1
    self.t = 1
    self.dt = 0.02
    self.collis = False
    self.not_colid = True
    self.first_collid = False
    self.motion0 = 0
    self.angle = 360
    self.angle_col = 0
    self.after_collid = 0
    self.rect = self.surface.get_rect(center=(self.rect.x - pygame.Surface.get_width(self.surface)/2, self.rect.y - pygame.Surface.get_height(self.surface)/2))

    self.main_speed = [self.vx, self.vy, self.angle]


  def move(self, win, event, n = 2):
      center = self.rect.center

      if event == 3:
        #print("Davo equals hambality,")
        #print(self.rect.center)
        
        #print(self.x, ' ', self.y)
        #print(self.rect.center)
        center = self.rect.center
        self.angle = (self.angle - 5) % 360
        
        #print(self.angle)

      if event == 4:
        center = self.rect.center
        self.angle = (self.angle + 5) % 360
      

      if event == 134:
        center = self.rect.center
        self.angle = (self.angle - ((-1)**n) * self.speed/2) % 360
        #print(self.angle)

      if event == 234:
        center = self.rect.center
        self.angle = (self.angle + ((-1)**n) * self.speed/2) % 360
      
      image = pygame.transform.rotate(self.surface, self.angle)
      self.rect = image.get_rect()
      self.rect.center = center

      if event == 134:

        self.y -= self.vx * math.cos(math.radians(360-self.angle))
        self.x += self.vy * math.sin(math.radians(360-self.angle))
        self.rect.y = self.y
        self.rect.x = self.x
        if self.start > 0:
          self.rect.center = (self.rect.x - int(pygame.Surface.get_width(self.surface)/2), self.rect.y - int(pygame.Surface.get_height(self.surface)/2))
        if self.start == 0:
          self.start = 1
          self.rect.center = (self.rect.x - int(pygame.Surface.get_width(self.surface)/2), self.rect.y - int(pygame.Surface.get_height(self.surface)/2))
          


      if event == 234:

        self.y += self.vx * math.cos(math.radians(360-self.angle))
        self.x -= self.vy * math.sin(math.radians(360-self.angle))
        self.rect.y = self.y
        self.rect.x = self.x 
        if self.start > 0:
          self.rect.center = (self.rect.x - int(pygame.Surface.get_width(self.surface)/2), self.rect.y - int(pygame.Surface.get_height(self.surface)/2))
        if self.start == 0:
          self.start = 1
          self.rect.center = (self.rect.x - int(pygame.Surface.get_width(self.surface)/2), self.rect.y - int(pygame.Surface.get_height(self.surface)/2))
          
 
      
      if event == 1:
          #print(self.angle)
          #rint(self.x, ' ', self.y)
          #print(self.rect.x, ' ', self.rect.y)
          #if self.start == 1:
           # self.rect.center = (self.rect.x - int(pygame.Surface.get_width(self.surface)/2), self.rect.y - int(pygame.Surface.get_height(self.surface)/2))

          self.y -= self.vy * math.cos(math.radians(360-self.angle))
          self.x += self.vx * math.sin(math.radians(360-self.angle))
          self.rect.y = self.y
          self.rect.x = self.x
          #print(self.x, ' ', self.y)
          #print(self.rect.x, ' ', self.rect.y)
          #print(self.angle)
          #print("End,")
          if self.start > 0:
            self.rect.center = (self.rect.x - int(pygame.Surface.get_width(self.surface)/2), self.rect.y - int(pygame.Surface.get_height(self.surface)/2))
          if self.start == 0:
            self.start = 1
            self.rect.center = (self.rect.x - int(pygame.Surface.get_width(self.surface)/2), self.rect.y - int(pygame.Surface.get_height(self.surface)/2))
         # print(self.start)

          
         
      if event == 2:
        self.y += self.vy * math.cos(math.radians(360-self.angle))
        self.x -= self.vx  * math.sin(math.radians(360-self.angle))
        self.rect.y = self.y
        self.rect.x = self.x
        if self.start > 0:
          self.rect.center = (self.rect.x - int(pygame.Surface.get_width(self.surface)/2), self.rect.y - int(pygame.Surface.get_height(self.surface)/2))
        if self.start == 0:
          self.start = 1
          self.rect.center = (self.rect.x - int(pygame.Surface.get_width(self.surface)/2), self.rect.y - int(pygame.Surface.get_height(self.surface)/2))
          

      

      if self.rect.top >= HEIGHT:
        self.kill()

      #print(self.angle)
      pygame.draw.rect(self.surface, self.color, (0, 0, self.side1, self.side2))
      win.blit(image, self.rect)


  def collisions(self, obj):
    if self.rect.colliderect(obj.rect):
      self.angle_col = abs(self.angle - obj.angle)

      '''
      image = pygame.transform.rotate(self.surface, self.angle)
      self.rect = image.get_rect()
      #print(self.rect.x, obj.rect.x, self.rect.y, obj.rect.y, self.x - obj.rect.x )
      
      self.x += (self.x - obj.rect.x)/abs(self.x - obj.rect.x) * math.sin(math.radians(360-self.angle))
      self.y -=(-1) * (self.y - obj.rect.y)/abs(self.y - obj.rect.y) * math.cos(math.radians(360-self.angle))
      
      self.rect.x = self.x
      self.rect.y = self.y
      
      self.rect.center = (self.rect.x - int(pygame.Surface.get_width(self.surface)/2), self.rect.y - int(pygame.Surface.get_height(self.surface)/2))
      #print(self.rect.y, self.rect.x, obj.rect.x, obj.rect.y)
      

      pygame.draw.rect(self.surface, self.color, (0,0, self.side1, self.side2))
      win.blit(image, self.rect)
      '''
      self.collis = True
      
      return obj
 
  def col_update(self):
    
    self.t += self.dt
    print(self.t)

    
    if self.vx <= 5 and self.vy <= 5:
      self.vy += 2
      self.vx += 2
      


    image = pygame.transform.rotate(self.surface, self.angle)
    self.rect = image.get_rect()

    self.rect.x = self.x
    self.rect.y = self.y
    
    self.rect.center = (self.rect.x - int(pygame.Surface.get_width(self.surface)/2), self.rect.y - int(pygame.Surface.get_height(self.surface)/2))

    pygame.draw.rect(self.surface, self.color, (0,0, self.side1, self.side2))
    win.blit(image, self.rect)

    if self.t >= 1:
      self.not_colid = True
      self.collis = False
      self.after_collid = 1
      print("111111111111")



   
  def update(self, win, motion, n):
    print(self.collis, self.not_colid, self.t)
    if self.collis and self.t >= 1:
      print(222222222)
      self.t = 0
      self.vx = 0
      self.vy = 0
      self.not_colid = False
    if self.not_colid == False:
      self.after_collid = 0
      self.col_update()
    if self.not_colid == True:
      print("!!!", motion)

      if self.after_collid == 1 and (motion == self.motion0 or int(motion/100) == self.motion0):
        print(3333333)
        self.t = 0
        self.vx = 0
        self.vy = 0
        self.col_update()
        self.not_colid = False
        print("!!!!!!!", self.motion0)

      else:
        self.move(win, motion, n)
        self.after_collid = 0
        if motion > 0:
          self.motion0 = motion
          print("!", self.motion0)

 

     

road1 = Road(100, 0)
road2 = Road(0, 100)
road3 = Road(500, 0)
roads_ver1 = [road1.center1, road3.center1]
roads_ver2 = [road1.center2, road3.center2]
roads_gor1 = [road2.center1]
roads_gor2 = [road2.center2]

if __name__ == '__main__':
    pygame.init()
    SCREEN = WIDTH, HEIGHT = 1200, 800
    win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)

    clock = pygame.time.Clock()
    FPS = 60
    count = 0

    square_group1 = pygame.sprite.Group()
    square_group2 = pygame.sprite.Group()
    square_group3 = pygame.sprite.Group()
    square_group4 = pygame.sprite.Group()
    square_group_main = pygame.sprite.Group()    

    running = True
    while running:
        win.fill((255,255,255))

        count += 0.5
        if count % 100 == 0:
          if i == 0:
            car_main = Square_main(200 , 300)
           # car_main.parametrs()
            square_group_main.add(car_main)
            
            i += 1 
          x = choice(roads_ver1 + roads_ver2 + coord_gor)
          if x == 0:
            y = choice(roads_gor1)
            square = Square(x, y)
            square_group1.add(square)
          if x == width:
            y = choice(roads_gor2)
            square = Square(x, y)
            square_group2.add(square)
          else:
            if x in roads_ver1:
              y = 0
              square = Square(x, y)
              square_group3.add(square)
            if x in roads_ver2:
              y = height
              square = Square(x, y)
              square_group4.add(square)

            
        road1.drawing(win)
        road2.drawing(win)
        road3.drawing(win)

        
        cars = square_group1.sprites() + square_group2.sprites() + square_group3.sprites() + square_group4.sprites()
        

        for event in pygame.event.get():
          keys = pygame.key.get_pressed()
            #if event.type == pygame.KEYDOWN:
          if keys[pygame.K_ESCAPE]:
            running = False

          if keys[pygame.K_w] :
            motion = 1
            #print(1)

          if keys[pygame.K_s]:
            motion = 2
          if keys[pygame.K_d]:
            motion = 3
          if keys[pygame.K_a]:
            motion = 4
          if keys[pygame.K_w] and keys[pygame.K_d] or (keys[pygame.K_w] and keys[pygame.K_a]):
            motion = 134
            if keys[pygame.K_w] and keys[pygame.K_d]:
              n = 2
            if keys[pygame.K_w] and keys[pygame.K_a]:
              n = 1

          if (keys[pygame.K_s] and keys[pygame.K_d]) or (keys[pygame.K_s] and keys[pygame.K_a]):
            motion = 234
            if keys[pygame.K_s] and keys[pygame.K_d]:
              n = 2
            else:
              n = 1

         
          if not keys[pygame.K_w] and not keys[pygame.K_d] and not keys[pygame.K_a] and not keys[pygame.K_s]: 
            motion = 0
    
        

         # print(type(car[0]))
        square_group_main.update(win, motion, n)
        for r in range(0,len(cars)):
          car_main.collisions(cars[r]) 
          if car_main.collisions(cars[r]) :
            square_group_main.update(win, motion, n)
            cars[r].collisions(car_main)

        square_group1.update(win, 2, 1, 90)
        square_group2.update(win, 1, 1, 90)
        square_group3.update(win, 2)
        square_group4.update(win, 1)
            

        #pygame.draw.rect(win, (30,30,30), (0, 0, WIDTH, HEIGHT), 8)
        clock.tick(FPS)
        pygame.display.update()
