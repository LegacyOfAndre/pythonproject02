#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.display
from pygame import Surface

from codes.Entity import Entity
from codes.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option  # option that you choose play mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity("imagebackground"))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surfaces, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass
