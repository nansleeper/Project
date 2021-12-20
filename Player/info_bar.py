import pygame
from Player.player import Player

def show_infobar(screen, player):
    '''
    Функция отрисовывает строку информации сверху.
    screen - экран на котором она отрисовывается
    player - персонаж, чьё состояние оно отображает
    '''
    info_screen = pygame.image.load('Core/texture/fonmain.bmp')
    screen.blit(info_screen, (0, 0))
    pygame.draw.polygon(screen, (255, 250, 0),
                        ((120, 15), (172, 45), (172, 105), (120, 135), (68, 105), (68, 45), (120, 15)))
    pygame.draw.polygon(screen, (248, 250, 251),
                        ((120, 25), (163, 50), (163, 100), (120, 125), (77, 100), (77, 50), (120, 25)))
    pygame.draw.polygon(screen, (255, 165, 0),
                        ((120, 15), (172, 45), (172, 105), (120, 135), (68, 105), (68, 45), (120, 15)), 5)
    pygame.draw.rect(screen, (255, 255, 255), (200, 40, 310, 70), 3)
    pygame.draw.rect(screen, (155, 0, 0), (205, 45, 3 * player.health, 60))
    if player.car:
        icon_screen = pygame.image.load('Core/texture/carico.bmp')
        icon_screen.set_colorkey((248, 250, 251))
        screen.blit(icon_screen, (68, 30))
    elif player.fire:
        icon_screen = pygame.image.load('Core/texture/fireico.bmp')
        icon_screen.set_colorkey((255, 255, 255))
        screen.blit(icon_screen, (90, 40))
    else:
        icon_screen = pygame.image.load('Core/texture/playerico.bmp')
        icon_screen.set_colorkey((248, 250, 251))
        screen.blit(icon_screen, (70, 30))