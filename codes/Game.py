#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from codes.Constantes import WINDOWS_WIDTH
from codes.Constantes import WINDOWS_HEIGHT
from codes.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOWS_WIDTH, WINDOWS_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
