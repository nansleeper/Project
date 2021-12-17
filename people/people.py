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


class Human:
    minFahm = 10 ** 18
    def __init__(self, x, y, r=30):
        Human.minFahm -= 1
        self.fahm = Human.minFahm
        self.coords = (x, y)
        self.velocity = (0, 0)
        min_velocity = 3.
        while self.velocity[0] * self.velocity[0] + self.velocity[1] + self.velocity[1] < min_velocity * min_velocity:
            self.velocity = np.random.randint(-4 * min_velocity, 4 * min_velocity, size=(2)).astype(float)
        self.velocity = (self.velocity[0], self.velocity[1])

        self.orientation = 0
        self.wishedOrientation = 0

        if type(r) in (tuple, list, np.array):
            self.r = random.uniform(r[0], r[1])
        else:
            self.r = r

        self.surface = pygame.Surface((2 * self.r, 2 * self.r), pygame.SRCALPHA)
        self.surface.set_colorkey((255, 255, 255))
        self.rect = self.surface.get_rect(center=(x, y))

        self.is_alive = True


    def move(self, dt = 1, Map_activesectors = []):
        rotation = 10
        self.orientation = self.wishedOrientation;
        for attempts in range(360 // rotation + 1):
            class Dzu:
                pass
            copy = Dzu()
            copy.coords = cp.deepcopy(self.coords)
            copy.r = cp.deepcopy(self.r)
            copy.coords = vector_sum(copy.coords, self.velocity * dt)
            canMove = True
            for idiot in people:
                if idiot != self and idiot.is_alive and idiot.collides1(copy):
                    if self.fahm < idiot.fahm:
                        return
                    #print(idiot.coords, ' ', copy.coords)
                    canMove = False
            for sector in Map_activesectors:
                if sector in ['CrossRoad', 'HorRoad', 'VertRoad', \
                'VertRoadUnable', 'HorRoadUnable', 'DownBorder', 'LeftBorder', \
                'UpBorder', 'RightBorder', 'Water', 'Bridge'] and \
                self.collides2(sector.center, 300):
                    canMove = False
                    self.wishedOrientation = self.orientation
            if canMove == True:
                self.coords = cp.deepcopy(copy.coords)
                return
                # print("Rotating...")
            self.orientation += rotation
            self.velocity = (self.velocity[0] * math.cos(rotation) - self.velocity[1] * math.sin(rotation),
                             self.velocity[0] * math.sin(rotation) + self.velocity[1] * math.cos(rotation))
        Human.minFahm -= 1
        fahm = Human.minFahm


    def collides1(self, rhs):
        distance = ((self.coords[0] - rhs.coords[0]) ** 2 + (self.coords[1] - rhs.coords[1]) ** 2) ** 0.5
        return distance < self.r + rhs.r


    def collides2(self, center, side):
        for c in (0, 1):
            for border in (center[c] - side / 2, center[c] + side / 2):
                if math.abs(self.coords[c] - border) < self.r:
                    return True
        for vertex in ((center[c] - side / 2, center[c] - side / 2), \
                       (center[c] - side / 2, center[c] + side / 2), \
                       (center[c] + side / 2, center[c] - side / 2), \
                       (center[c] + side / 2, center[c] + side / 2)):
            if point_distance(self.coords, vertex) < self.r:
                return True
        return False


    def render(self):
        surface=self.surface
        if self.is_alive:
            koldunov = pygame.image.load('people/koldunov.jpg')
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


GREY = (77, 77, 77)
BLACK = (0, 0, 0)
WHIGHT = (255, 255, 255)
GREEN = (204, 255, 102)
PINK = (255, 102, 255)
COLOR = [GREEN, PINK]

screen = pygame.display.set_mode((800, 1000))
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
    zibil = 5
    for i in range(zibil):
        for j in range(zibil):
            people.append(Human((i + 1) * 800 / (zibil + 1),
                                (j + 1) * 800 / (zibil + 1), (30, 40)))


def movePeople():
    for idiot in people:
        idiot.move()


#if __name__ == '__main__':
def run_randomly_eat_stuff(Map_activesectors):
    pygame.init()
    initPeople()
    SCREEN = (WIDTH, HEIGHT) = (1200, 800)
    win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)

    while True:
        pygame.display.update()
        clock = pygame.time.Clock()
        clock.tick(FPS)
        display.fill((0, 0, 0))
        for idiot in people:
            if idiot.is_alive:
                idiot.move(1, Map_activesectors)
                idiot.render()
        pygame.display.update()

do_shit([])
