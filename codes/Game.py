#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from codes.Constantes import WINDOWS_WIDTH, WINDOWS_HEIGHT, MENU_OPTION
from codes.Level import Level
from codes.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOWS_WIDTH, WINDOWS_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, "Level 1", menu_return)
                level_return = level.run()
            else:
                pygame.quit()
                sys.exit()

