#!/usr/bin/python

'''
http://www.pygame.org/docs/tut/newbieguide.html

cd C:\sers\Gerardo\Documents\Projects\Local
py
>>>import pygame
>>>pygame.version.ver
'1.9.2a0'
>>>exit()
py pygametutorial.py
'''

# window

import sys, pygame
pygame.init()

size = width, height = 320, 240
menu = True

while menu:
    print ("""
    0) Exit/Quit
    1) Fixed Size
    2) Custom Size
    3) Resizable
    4) Full Screen
    5) Extra!
    """)

    menu = input("Introduce the window size option: ")
    if menu == "0":
        exit()
    elif menu == "1":
        screen = pygame.display.set_mode(size)
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
    elif menu == "2":
        x = int(input("Width: "))
        y = int(input("Height: "))
        size = x, y
        screen = pygame.display.set_mode(size)
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
    elif menu == "3":
        screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
    elif menu == "4":
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: sys.exit()
    elif menu == "5":   # quit the window but not the program
        running = True
        screen = pygame.display.set_mode(size)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
    else:
        print("\nNot valid choice. Try again!")
