#import /home/rubo/qaq/people/people.py as People
import pygame
import people.people as People

def init_people(people):
    zibil = 5
    for i in range(zibil):
        for j in range(zibil):
            people = People.birth(people, (i + 1) * 800 / (zibil + 1), (j + 1) * 800 / (zibil + 1))
    return people

pygame.init()
FPS = 5
SIDES = [1690, 690]
display = pygame.display.set_mode(SIDES)
pygame.display.update()
clock = pygame.time.Clock()
pygame.init()
people = []
people = init_people(people)
SCREEN = (WIDTH, HEIGHT) = (1200, 800)
win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
Map_activesectors = []
while True:
    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(FPS)
    display.fill((123, 23, 34))
    people = People.tick(display, people, Map_activesectors)
    pygame.display.update()
