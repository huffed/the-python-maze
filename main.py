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
class colours:
    white = (255, 255, 255)
    black = (0, 0, 0)

class images:
    bg = pygame.image.load('./images/bg/bg.png')
    icon = pygame.image.load('./images/icon/the-python-maze-icon.png')

class windowSettings:
    res = 1280, 720
    font = pygame.font.Font('./font/pixel-font.ttf', 30)

class settings:
    fps = 15
    speed = 20
    clock = pygame.time.Clock()

class player:
    playerImg = pygame.image.load('./images/user/knight.png')
    playerX = 200
    playerY = 200
    playerX_change = 0
    playerY_change = 0

# creates the screen and changes icon
window = pygame.display.set_mode(windowSettings.res)
icon = pygame.display.set_icon(images.icon)

# FUNCTIONS START

def playerxy(x, y):
    window.blit(player.playerImg, (x, y))

# runtime welcome screen
def welcome():
    window.blit(images.bg, (0, 0))
    pygame.display.set_caption('The Python Maze - Welcome')
    playing = True

# main game screen
def main():
    window.blit(images.bg, (0, 0))
    pygame.display.set_caption('The Python Maze')

# RUNTIME
running = True
while running:

    window.fill(colours.black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # keydown events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -abs(settings.speed)
            elif event.key == pygame.K_RIGHT:
                playerX_change = settings.speed
            elif event.key == pygame.K_UP:
                playerY_change = settings.speed
            elif event.key == pygame.K_DOWN:
                playerY_change = -abs(settings.speed)
        # keyup events
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0

    welcome()
    main()

    player.playerX += player.playerX_change
    if player.playerX <= 0:
        player.playerX = 0
    elif player.playerX >= 736:
        player.playerX = 736

    playerxy(player.playerX, player.playerY)

    pygame.display.flip()
