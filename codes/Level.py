#!/usr/bin/python
#-*- coding: utf-8 -*-
from codes.Entity import Entity


class Level:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.mode = menu_option # option that you choose play mode
        self.entity_list = list[Entity] = []

    def run(self, ):
        pass

