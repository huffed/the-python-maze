#!/usr/bin/env python3

"""
The Python Maze

This is a simple maze game made in preperation to my GCSE project.

Author: Jack Jones
School: Stover School
Year: 11
Teacher: Ben Kerr
"""

import pygame
import math
import sys
import time

# initializing the constructor
pygame.init()

# DEFINING GLOBAL VARIABLES

class widgetSettings:
    button = pygame.Rect(0,0,0,0)

class colours:
    white = (255, 255, 255)
    black = (0, 0, 0)
    grey = (90, 90, 90)

class images:
    bg = pygame.image.load('./images/bg/bg.png')
    icon = pygame.image.load('./images/icon/the-python-maze-icon.png')

class windowSettings:
    res = 1280, 720
    font = pygame.font.Font('./font/pixel-font.ttf', 30)

class settings:
    fps = 15
    speed = 3
    clock = pygame.time.Clock()
    mouse_pos = ""

class player:
    playerImg = pygame.image.load('./images/user/knight.png')
    playerImgResize = pygame.transform.scale(playerImg, (100, 100))
    playerX = 200
    playerY = 200
    playerX_change = 0
    playerY_change = 0

class widgets:
    # defining button structure
    def button(msg,x,y,w,h,adjustX,adjustY,inactiveColour,activeColour,textColour,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        widgetSettings.button.width = w
        widgetSettings.button.height = h
        widgetSettings.button.x = x
        widgetSettings.button.y = y
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(window, activeColour, (x,y,w,h))
            if click[0] == 1 and action != None:
                action
        else:
            pygame.draw.rect(window, inactiveColour, (x,y,w,h))
        text = windowSettings.font.render(msg, True, textColour)
        center = ((x+(w/2)-adjustX)), y+((h/2)-adjustY)
        window.blit(text,center)

    # defining text box structure
    def textBox(msg,x,y,w,h,adjustX,adjustY,colour,textColour):
        widgetSettings.button.width = w
        widgetSettings.button.height = h
        widgetSettings.button.x = x
        widgetSettings.button.y = y
        pygame.draw.rect(window, colour, (x,y,w,h))
        text = windowSettings.font.render(msg, True, textColour)
        center = ((x+(w/2)-adjustX)), y+((h/2)-adjustY)
        window.blit(text,center)

# creates the screen and changes icon
window = pygame.display.set_mode(windowSettings.res)
pygame.font.init()
icon = pygame.display.set_icon(images.icon)

def events():
    # keydown events
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player.playerX_change -= settings.speed
        elif event.key == pygame.K_RIGHT:
            player.playerX_change += settings.speed
        elif event.key == pygame.K_UP:
            player.playerY_change -= settings.speed
        elif event.key == pygame.K_DOWN:
            player.playerY_change += settings.speed
    # keyup events
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            player.playerX_change = 0
            player.playerY_change = 0

def playerxy(x, y):
    window.blit(player.playerImgResize, (x, y))

def quitGame():
    running = False
    pygame.quit()
    quit()

# runtime welcome screen
def welcome():
    mouse = pygame.mouse.get_pos()
    window.blit(images.bg, (0, 0))
    pygame.display.set_caption('The Python Maze - Welcome')
    widgets.textBox("The Python Maze",360,125,500,100,220,10,colours.black,colours.white)
    widgets.button("START",250,450,250,80,70,10,colours.black,colours.grey,colours.white,main())
    widgets.button("QUIT",750,450,250,80,60,10,colours.black,colours.grey,colours.white,quitGame())
#     def button1():
#         widgetSettings.button.width = 250
#         widgetSettings.button.height = 80
#         # draw button1
#         if widgetSettings.button.x+widgetSettings.button.width > mouse[0] > widgetSettings.button.x and widgetSettings.button.y+widgetSettings.button.height > mouse[1] > widgetSettings.button.y:
#             pygame.draw.rect(window, colours.grey, widgetSettings.button)
#         else:
#             pygame.draw.rect(window, colours.black, widgetSettings.button)
#         text = windowSettings.font.render("Start", True, colours.white)
# #        textRect = text.get_rect(center=(windowSettings.res[0]/2, windowSettings.res[1]/2))
#         center = ((widgetSettings.button.x+((widgetSettings.button.width/2)-70)), widgetSettings.button.y+((widgetSettings.button.height/2)-10))
#         window.blit(text, center)
#     button1()

# main game screen
def main():
    window.blit(images.bg, (0, 0))
    pygame.display.set_caption('The Python Maze')
    playerxy(player.playerX, player.playerY)

# RUNTIME
running = True
stage = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        events()

    window.fill(colours.black)

    if stage == 1:
        welcome()
    elif stage == 2:
        main()

    # x change borders
    player.playerX += player.playerX_change
    if player.playerX <= 0:
        player.playerX = 0
    elif player.playerX >= 1100:
        player.playerX = 1100
    # y change borders
    player.playerY += player.playerY_change
    if player.playerY <= -12:
        player.playerY = -12
    elif player.playerY >= 535:
        player.playerY = 535

    pygame.display.update()
