# COOKIES = 0
# CPS = 0.0

import globalvar
import sys
import pygame
from pygame.locals import *
from constants import *
from classes import Item
from anteater import Anteater
# from sendgrid_python import sendgrid




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
    globalvar.COOKIES += 1


items = make_items(["1st Years", "HackUCI", "Taco Bell", "In N Out", "UTC", "ARC", "Aldrich Park", "Student Center",
                    "ICS", "Peter", "EECS"],
                   [15, 100, 500, 3000, 10000, 40000, 200000, 1700000, 150000000, 5000000000, 70000000000],
                   [0.1, 0.5, 4, 10, 40, 100, 400, 5000, 90000, 1000000, 10000000],
                   Rect(400, 25, 230, 400), 5)


def calculate_cps():
    global CPS
    cps = 0.0
    for item in items:
        cps += item.total_cps()
    globalvar.CPS = cps

def update_cookies():
    global COOKIES
    globalvar.COOKIES += globalvar.CPS / FPS

def belly_bot():
    globalvar.belly+=1


# client = sendgrid.SendGridClient("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")
# message = sendgrid.Mail()

# message.add_to("kseme001@ucr.edu")
# message.set_from("jlee401@ucr.edu")
# message.set_subject("Sending with SendGrid is Fun")
# message.set_html("and easy to do anywhere, even with Python")

# client.send(message)

counter = 1

while True:
    screen.fill(BLACK)
    screen.blit(BACKGROUND_IMAGE, Rect(0,0,640 ,480))
    screen.blit(ANTEATER_IMAGE, anteater.ant_rect)

    #draw cookies count
    text_surface = FONT.render(str(int(globalvar.COOKIES)) + " Zots" + " + "+ str(globalvar.CPS) + "Zot/Sec", False, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (100, 200)
    screen.blit(text_surface, text_rect)


    #draw percentage
    belly_surface = FONT.render("Belly = "+str(globalvar.belly)+ "%", False, WHITE)
    belly_rect = belly_surface.get_rect()
    belly_rect.topleft = (0, 50)
    screen.blit(belly_surface, belly_rect)


    if (globalvar.CPS > 0.8):
    	counter = 2
    if (globalvar.CPS > 1.4):
    	counter = 3
    if (globalvar.CPS > 5):
    	counter = 4
    if (globalvar.CPS > 10):
    	counter = 5
    if (globalvar.CPS > 30):
    	counter = 6
    if (globalvar.CPS > 100):
    	counter = 7
    if (globalvar.CPS > 325):
    	counter = 8
    if (globalvar.CPS > 3000):
    	counter = 9
    if (globalvar.CPS > 50000):
    	counter = 10
    if (globalvar.CPS > 600000):
    	counter = 11
    if (globalvar.CPS > 7000000):
    	counter = 12

    i = 0

    for button in items:
        if (i < counter):
        	button.draw(screen)
        	i += 1

    calculate_cps()
    update_cookies()

    
    
    for event in pygame.event.get():
        if globalvar.COOKIES % 100 == 0 and globalvar.COOKIES != 0 and globalvar.COOKIES % 300 != 0:
            pygame.mixer.music.load('Success.mp3')
            pygame.mixer.music.play(0)
        if globalvar.COOKIES % 300 == 0 and globalvar.COOKIES != 0:
            pygame.mixer.music.load('OhBabyATriple.mp3')
            pygame.mixer.music.play(0)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #hotkey for 'z' press
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            if key_name == 'z':
                if globalvar.belly>=0:
                    click_cookie()
                    globalvar.belly-=.25
        #hotkey for mouse click
        elif event.type == MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            mouse_button = event.button
            if mouse_button == 1:
                #belly logic
                if globalvar.belly<=99:
                    
                for button in items:
                    if button.collidepoint(mouse_pos):
                        button.click()
                        break
                if anteater.ant_rect.collidepoint(mouse_pos):
                    if globalvar.belly>=0:
                        click_cookie()
                        globalvar.belly-=.25

        
                    

    pygame.display.update()
    fpsClock.tick(FPS)
