#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from codes.Constantes import WINDOWS_WIDTH, COLOR_BLACK, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load("../assets/menu/menu_background/menu_background.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load("../assets/menu/menu_background/menu_background.wav")
        pygame.mixer_music.play(-1)
        menu_option = 0
        while True:
            # Desenhar na tela
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Desaster", COLOR_BLACK, ((WINDOWS_WIDTH / 3), 40))
            self.menu_text(25, "in the", COLOR_BLACK, ((WINDOWS_WIDTH / 2), 80))
            self.menu_text(50, "Sky", COLOR_BLACK, ((WINDOWS_WIDTH / 1.5), 110))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WINDOWS_WIDTH / 2), 200 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_BLACK, ((WINDOWS_WIDTH / 2), 200 + 30 * i))

            pygame.display.flip()

            # Verificar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.window.blit(source=text_surf, dest=text_rect)
