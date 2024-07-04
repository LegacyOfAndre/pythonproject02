#!/usr/bin/python
# -*- coding: utf-8 -*-
from codes.Constantes import WINDOWS_WIDTH
from codes.background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case "imagebackground":
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f"imagebackground{i}", (0, 0)))
                    list_bg.append(Background(f"imagebackground{i}", (WINDOWS_WIDTH, 0)))
                return list_bg
