import sys
import pygame
from pygame.locals import *
from constants import *
from classes import Item
from anteater import Anteater


def make_items(text_list, base_price_list, cps_list, rect, spacing):
    button_height = rect.height / len(text_list)
    button_width = rect.width
    buttons = []
    for i in range(len(text_list)):
        text = text_list[i]
        base_price = base_price_list[i]
        base_cps = cps_list[i]
        button_rect = Rect(rect.left, rect.top + i * (button_height + spacing), button_width, button_height)
        button = Item(button_rect, text, base_price, base_cps)
        buttons.append(button)
    return buttons

anteater = Anteater(ANTEATER_IMAGE)
anteater.createA()


def click_cookie():
    global COOKIES
    COOKIES += 1


items = make_items(["Cursor", "Grandma", "Farm", "Factory", "Mine", "Shipment", "Alchemy Lab", "Portal",
                    "Time machine", "Antimatter condenser", "Prism"],
                   [15, 100, 500, 3000, 10000, 40000, 200000, 1666666, 123456789, 3999999999, 75000000000],
                   [0.1, 0.5, 4, 10, 40, 100, 400, 6666, 98765, 999999, 10000000],
                   Rect(400, 25, 230, 400), 5)


def calculate_cps():
    global CPS
    cps = 0.0
    for item in items:
        cps += item.total_cps()
    CPS = cps

def update_cookies():
    global COOKIES
    COOKIES += CPS / FPS

while True:
    screen.fill(BLACK)
    screen.blit(BACKGROUND_IMAGE, Rect(0,0,640 ,480))
    screen.blit(ANTEATER_IMAGE, anteater.ant_rect)

    #draw cookies count
    text_surface = FONT.render(str(int(COOKIES)) + " Zots" + " + "+ str(CPS) + "Zot/Sec", False, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (100, 200)
    screen.blit(text_surface, text_rect)

    for button in items:
        button.draw(screen)

    calculate_cps()
    update_cookies()

    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #hotkey for 'z' press
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            if key_name == 'z':
                click_cookie()
        #hotkey for mouse click
        elif event.type == MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            mouse_button = event.button
            if mouse_button == 1:
                for button in items:
                    if button.collidepoint(mouse_pos):
                        button.click()
                        break
                if anteater.ant_rect.collidepoint(mouse_pos):
                    click_cookie()
                    

    pygame.display.update()
    fpsClock.tick(FPS)
