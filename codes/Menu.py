#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from codes.Constantes import WINDOWS_WIDTH

class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('C:\pythonprojeto02\essets\menu\menu_background.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load("C:\pythonprojeto02\essets\menu\menu_sound.wav")
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Desaster", (145, 0, 2), ((WINDOWS_WIDTH / 3), 40))
            self.menu_text(25, "in the", (0, 0, 0), ((WINDOWS_WIDTH / 2), 80))
            self.menu_text(50, "Sky", (145, 0, 2), ((WINDOWS_WIDTH / 1.5), 110))
            pygame.display.flip()
        pass

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.window.blit(source=text_surf, dest=text_rect)
