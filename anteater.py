import pygame
import sys
from pygame.locals import *

class Anteater:
    def __init__(self, image):
        self.image = image
    def createA(self):
        self.ant_rect= Rect(15, 200, self.image.get_width(), self.image.get_height())
    def move(self):
        self.ant_rect= Rect(5, 200, self.image.get_width(), self.image.get_height())
    def remove(self):
        self.ant_rect= Rect(20, 200, self.image.get_width(), self.image.get_height())
                            



