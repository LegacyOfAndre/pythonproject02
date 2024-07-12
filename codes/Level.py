#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from codes.Constantes import COLOR_WHITE, MENU_OPTION, EVENT_ENEMY
from codes.Entity import Entity
from codes.EntityFactory import EntityFactory
from codes.EntityMediator import EntityMediator


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option  # option that you choose play mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity("imagebackground"))
        self.entity_list.append(EntityFactory.get_entity("Player1"))
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity("Player2"))
        pygame.time.set_timer(EVENT_ENEMY, 4000)

    def run(self):
        clock = pygame.time.Clock()
        pygame.mixer_music.load("../assets/assets_background_level_one/level_one_background.wav")
        pygame.mixer_music.play(-1)

        while True:
            clock.tick(60)  # tick to select the fps

            # for to draw all entities
            for ent in self.entity_list:
                self.window.blit(source=ent.surfaces, dest=ent.rect)  # here is drawing all entities
                ent.move()

            # printing the fps text in the window
            self.level_text(14, f"Fps: {clock.get_fps():.0f}", COLOR_WHITE, (10, 10))
            self.level_text(14, f"Entities: {len(self.entity_list)}", COLOR_WHITE, (10, 25))

            # reload window
            pygame.display.flip()

            # verify relationships of entities
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            # check events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(("Enemy1", "Enemy2"))
                    self.entity_list.append(EntityFactory.get_entity(choice))
        pass

    # method that define the text level font
    def level_text(self, text_size: int, text: str, text_color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_position[0], top=text_position[1])
        self.window.blit(source=text_surf, dest=text_rect)
