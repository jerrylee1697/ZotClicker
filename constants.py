import sys
import pygame
from pygame.locals import *

SIZE = (640, 480)
FPS = 30




pygame.init()

fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("zotclicker")

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

BUTTON_BG_COLOR = pygame.Color(178, 176, 176)
BUTTON_BORDER_COLOR = pygame.Color(85, 50, 232)

FONT = pygame.font.SysFont("Arial", 20, True)

ANTEATER_IMAGE = pygame.image.load("anteater.png")
BACKGROUND_IMAGE = pygame.image.load("background.jpg")

