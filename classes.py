import pygame
import sys
from pygame.locals import *
from constants import *
import globalvar

class Item:
    def __init__(self, rect, text, base_price, base_cps_each):
        self.rect = rect
        self.text = text
        self.count = 0
        self.base_price = base_price
        self.cps_each = base_cps_each

    def draw(self, surface):
        #draw background
        pygame.draw.rect(surface, BUTTON_BG_COLOR, self.rect, 0)
        #draw border
        pygame.draw.rect(surface, BUTTON_BORDER_COLOR, self.rect, 2)
        #draw text
        text_surface = FONT.render(str(self.count) + "x" + self.text + " $" + str(int(self.price())), False, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.rect.left + 10, self.rect.top + self.rect.height * 0.25)
        surface.blit(text_surface, text_rect)
        
    def drawbelly(self, surface):
        #draw background
        pygame.draw.rect(surface, BUTTON_BG_COLOR, self.rect, 0)
        #draw border
        pygame.draw.rect(surface, BUTTON_BORDER_COLOR, self.rect, 2)
        #draw text
        text_surface = FONT.render(self.text + " $" + str(int(self.price())), False, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.rect.left + 10, self.rect.top + self.rect.height * 0.25)
        surface.blit(text_surface, text_rect)
        
    def total_cps(self):
        return self.cps_each * self.count


    def price(self):
        return self.base_price * 1.15**self.count

    def click(self):
        price = self.price()
        global COOKIES
        if globalvar.COOKIES >= price:
            self.count += 1
            globalvar.COOKIES -= price

    def collidepoint(self, point):
        return self.rect.collidepoint(point)

