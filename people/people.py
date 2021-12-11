import math
import numpy as np
import pygame
import random
from pygame.draw import *
from random import randint
from random import choice
import math


class Ball:
    def __init__(self, x, y, r=30):
        self.coords = (x, y)
        self.velocity = (0, 0)
        min_velocity = 1.
        while self.velocity[0] * self.velocity[0] + self.velocity[1] + self.velocity[1] < min_velocity * min_velocity:
            self.velocity = np.random.randint(-4 * min_velocity, 4 * min_velocity, size=(2)).astype(float)

        self.orientation = 0

        if type(r) in (tuple, list, np.array):
            self.r = random.uniform(r[0], r[1])
        else:
            self.r = r

        self.surface = pygame.Surface((2 * self.r, 2 * self.r), pygame.SRCALPHA)
        self.surface.set_colorkey((255, 255, 255))
        self.rect = self.surface.get_rect(center=(x, y))

        self.is_alive = True

    def move(self, dt=1):
        rotation = 10
        for attempts in range(360 // rotation + 1):
            copy = self
            copy.coords += self.velocity * dt
            canMove = True
            for idiot in people:
                if idiot != copy and idiot.is_alive and copy.collision(idiot):
                    print(idiot.coords, ' ', copy.coords)
                    canMove = False
                # Check for collisions with buildings.
                i, j = copy.coords[0] // 600, copy.coords[1] // 600 # This shit is for debugging sake only. Should be replaced by the buildings collision check.
                if i % 2 == 0 and j % 2 == 0:
                    canMove = False
            if canMove == True:
                break
                # print("Rotating...")
            self.orientation += rotation
            self.velocity = (self.velocity[0] * math.cos(rotation) - self.velocity[1] * math.sin(rotation),
                             self.velocity[0] * math.sin(rotation) + self.velocity[1] * math.cos(rotation))
        self = copy

    def collision(self, rhs):
        distance = ((self.coords[0] - rhs.coords[0]) ** 2 + (self.coords[1] - rhs.coords[1]) ** 2) ** 0.5
        return distance < self.r + rhs.r

    def render(self):
        surface=self.surface
        if self.is_alive:
            koldunov = pygame.image.load('people//koldunov.jpg')
            koldunov.set_colorkey((0,0,0))
            koldunov = koldunov.convert_alpha()
            correct_scale = 2 * self.r
            correct_scale *= (abs(math.sin(self.orientation)) +
                              abs(math.cos(self.orientation)))
            correct_scale = math.ceil(2 * self.r / correct_scale)
            correct_scale = math.ceil(self.r)
            koldunov = pygame.transform.scale(koldunov, (correct_scale, correct_scale));
            koldunov = pygame.transform.rotate(koldunov, self.orientation);
            display.blit(koldunov, (self.coords[0] - self.r, self.coords[1] - self.r))

    def update(self):
        self.render(self.surface)

height = 800
width = 1000
score = 0
i = 0
motion = 0
n = 2

coord_gor = [0, width]

GREY = (77, 77, 77)
BLACK = (0, 0, 0)
WHIGHT = (255, 255, 255)
GREEN = (204, 255, 102)
PINK = (255, 102, 255)
COLOR = [GREEN, PINK]

screen = pygame.display.set_mode((width, height))
screen.fill(WHIGHT)


pygame.init()

FPS = 5
SIDES = [1690, 690]

display = pygame.display.set_mode(SIDES)

pygame.display.update()
clock = pygame.time.Clock()
gameover = False

people = []
def initPeople():
    peopleCount = 10
    for i in range(peopleCount):
        people.append(Ball((i + 1) * height / (peopleCount + 1),
                           width - (i + 1) * width / (peopleCount + 1), (30, 40)))

def movePeople():
    for idiot in people:
        idiot.move()

if __name__ == '__main__':
    pygame.init()
    initPeople()
    SCREEN = (WIDTH, HEIGHT) = (1200, 800)
    win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)

    while True:
        pygame.display.update()
        clock = pygame.time.Clock()
        clock.tick(FPS)
        display.fill((0, 0, 0))
        print("TICK")
        for idiot in people:
            if idiot.is_alive:
                idiot.move()
                idiot.render()
        pygame.display.update()
