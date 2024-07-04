#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surfaces = pygame.image.load("C:\pythonprojeto02\essets\image_background_level_one/" + name + ".png")
        self.rect = self.surfaces.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self):
        pass
