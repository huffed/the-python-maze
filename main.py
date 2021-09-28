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
from pygame import mixer
import math
import sys
import time
import logging
import tkinter as tk
from tkinter import messagebox
import base64
import zlib
import tempfile

# logging.basicConfig(filename='./log/info.log', filemode='w', format='%(process)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logging.basicConfig(filename='./log/error.log', filemode='w', format='%(process)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)
logging.basicConfig(filename='./log/debug.log', filemode='w', format='%(process)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

# initializing the constructor
pygame.init()
mixer.init()
logging.debug('constructor initialized')
stage = 1
logging.debug('stage variable set to 1')

# DEFINING GLOBAL VARIABLES

class widgetSettings:
    button = pygame.Rect(0,0,0,0)

class colours:
    white = (255, 255, 255)
    black = (0, 0, 0)
    grey = (90, 90, 90)

class images:
    bg = pygame.image.load('./images/bg/bg2.jpg')
    bgImgResize = pygame.transform.scale(bg, (1280,720))
    icon = pygame.image.load('./images/icon/the-python-maze-icon.png')
    playerImg = pygame.image.load('./images/user/knight.png')
    welcomeBg = pygame.image.load('./images/bg/welcome.png')
    startButtonInactive = pygame.image.load('./images/buttons/start-inactive.png')
    startButtonActive = pygame.image.load('./images/buttons/start-active.png')
    quitButtonInactive = pygame.image.load('./images/buttons/quit-inactive.png')
    quitButtonActive = pygame.image.load('./images/buttons/quit-active.png')
    audioOn = pygame.image.load('./images/buttons/audio-on.png')
    audioOff = pygame.image.load('./images/buttons/audio-off.png')
    mazeLvl1 = pygame.image.load('./images/maze/maze-lines-1.png')
    mazeLvl1Resize = pygame.transform.scale(mazeLvl1, (1280,720))

class windowSettings:
    res = 1280, 720
    #font = pygame.font.Font('./font/pixel-font.ttf', 30)

class settings:
    fps = 10
    fpsClock = pygame.time.Clock()
    speed = 10
    musicVolume = 0.7
    clock = pygame.time.Clock()
    mouse_pos = ""
    mixer.music.load('./sounds/music.mp3')
    mixer.music.set_volume(musicVolume)

class player:
    playerImgResize = pygame.transform.scale(images.playerImg, (100, 100))
    playerX = 1035
    playerY = 585
    playerX_change = 0
    playerY_change = 0

class widgets:
    # defining button structure
    def button(x,y,w,inactiveImage,activeImage,action=None):
        h = math.ceil(w/2.33)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        widgetSettings.button.width = w
        widgetSettings.button.height = h
        widgetSettings.button.x = x
        widgetSettings.button.y = y
        inactiveImageResize = pygame.transform.scale(inactiveImage, (w,h))
        activeImageResize = pygame.transform.scale(activeImage, (w,h))
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            window.blit(activeImageResize, (x,y))
            if click[0] == 1 and action != None:
                action()
        else:
            window.blit(inactiveImageResize, (x,y))
    # defining text box structure
    def textBox(msg,x,y,w,h,borderWidth,borderRadius,borderTopLeftRadius,borderTopRightRadius,borderBottomLeftRadius,borderBottomRightRadius,borderColour,adjustX,adjustY,colour,textColour):
        widgetSettings.button.width = w
        widgetSettings.button.height = h
        widgetSettings.button.x = x
        widgetSettings.button.y = y
        pygame.draw.rect(window, colour, (x,y,w,h))
        pygame.draw.rect(window, borderColour, (x-1,y-1,w+4,h+4), borderRadius, borderTopLeftRadius, borderTopRightRadius, borderBottomLeftRadius, borderBottomRightRadius)
        text = windowSettings.font.render(msg, True, textColour)
        center = ((x+(w/2)-adjustX)), y+((h/2)-adjustY)
        window.blit(text,center)

class transparentIcon:
    ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
        'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))
    _, ICON_PATH = tempfile.mkstemp()
    with open(ICON_PATH, 'wb') as icon_file:
        icon_file.write(ICON)

logging.debug('classes loaded')

# creates the screen and changes icon and initialized font
window = pygame.display.set_mode(windowSettings.res)
mixer.music.play()
audio = "on"
pygame.font.init()
icon = pygame.display.set_icon(images.icon)

logging.debug('screen loaded, icon changed and initialized font')

def events():
    # keydown events
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player.playerX_change -= settings.speed
            logging.debug('k_left pressed')
        elif event.key == pygame.K_RIGHT:
            player.playerX_change += settings.speed
            logging.debug('k_right pressed')
        elif event.key == pygame.K_UP:
            player.playerY_change -= settings.speed
            logging.debug('k_up pressed')
        elif event.key == pygame.K_DOWN:
            player.playerY_change += settings.speed
            logging.debug('k_down pressed')
    # keyup events
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            player.playerX_change = 0
            player.playerY_change = 0
            logging.debug('keyup (k_left,k_right,k_up,k_down)')
logging.debug('events function loaded')

def playerxy(x, y):
    window.blit(player.playerImgResize, (x, y))
logging.debug('playerxy function loaded')

def quitGame():
    global popUps
    popUp = messagebox.askquestion('Quit', 'Are you sure you want to quit?')
    if popUp == 'yes':
        pygame.quit()
        running = False
        quit()
    elif popUp == 'no':
        ""
    else:
        messagebox.showwarning('Error', 'Something went wrong!')
logging.debug('quitGame function loaded')

def gameStart():
    global stage
    stage = 2
    logging.debug('stage set to 2')
logging.debug('gameStart function loaded')

def audioOn():
    global audio
    mixer.music.unpause()
    audio = "on"
    logging.debug('audio on')

def audioOff():
    global audio
    mixer.music.pause()
    audio = "off"
    logging.debug('audio off')

# runtime welcome screen
def welcome():

    mouse = pygame.mouse.get_pos()
    logging.debug('mouse variable assigned')
    window.blit(images.welcomeBg, (0, 0))
    logging.debug("background blit'd")
    pygame.display.set_caption('The Python Maze - Welcome')
    logging.debug("title set to 'The Python Maze - Welcome'")
    widgets.button(110,320,300,images.startButtonInactive,images.startButtonActive,gameStart)
    logging.debug('start button loaded')
    widgets.button(110,480,300,images.quitButtonInactive,images.quitButtonActive,quitGame)
    logging.debug('quit button loaded')
    if audio == "on":
        widgets.button(-20,60,170,images.audioOn,images.audioOn,audioOff)
    elif audio == "off":
        widgets.button(-20,60,170,images.audioOff,images.audioOff,audioOn)
    logging.debug('audio toggle button loaded')
    logging.debug('buttons loaded')

# main game screen
def main():
    window.blit(images.bgImgResize, (0, 0))
    window.blit(images.mazeLvl1Resize, (0, 0))
    logging.debug('background for main loaded')
    pygame.display.set_caption('The Python Maze')
    logging.debug("title set to 'The Python Maze'")
    playerxy(player.playerX, player.playerY)
    logging.debug('playerxy function called')

# RUNTIME
running = True
logging.debug('running variable set to True')
while running:
    popUps = tk.Tk()
    logging.debug('tk window initialized')
    popUps.wm_withdraw()
    logging.debug('tk window withdrawn/hidden')
    popUps.iconbitmap(default=transparentIcon.ICON_PATH)
    logging.debug('tk window icon set to transparent icon')
    logging.debug('stage = {}'.format(stage))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            quit()
        events()
    logging.debug('quit event loaded inside loop')

    window.fill(colours.black)
    logging.debug('window fill set to colour-black')

    if stage == 1:
        welcome()
        logging.debug('welcome function called')
    elif stage == 2:
        main()
        logging.debug('main function called')

    # x change borders
    player.playerX += player.playerX_change
    if player.playerX <= -2:
        player.playerX = -2
    elif player.playerX >= 1191:
        player.playerX = 1191
    logging.debug('x change borders set')
    # y change borders
    player.playerY += player.playerY_change
    if player.playerY <= -7:
        player.playerY = -7
    elif player.playerY >= 627:
        player.playerY = 627
    logging.debug('y change borders set')

    # line collision
    for x1, y1, x2, y2 in walls:
        if x1 <= playerX <= x2 and y1 <= playerY <= y2:
            print("COLLIDE")
            return True
    return False

    pygame.display.update()
    logging.debug('display updated')
    settings.fpsClock.tick(settings.fps)
