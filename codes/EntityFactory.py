#!/usr/bin/python
# -*- coding: utf-8 -*-
from codes.background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position: tuple):
        match entity_name:
            case "imagebackground1":
                return Background(f"imagebackground1", position)
        pass