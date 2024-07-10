#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from codes.Constantes import WINDOWS_WIDTH, WINDOWS_HEIGHT
from codes.Enemy import Enemy
from codes.Player import Player
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

            case "Player1":
                return Player("Player1", (10, (WINDOWS_HEIGHT / 2 - 30)))

            case "Player2":
                return Player("Player2", (10, (WINDOWS_HEIGHT / 2 + 30)))

            case "Enemy1":
                return Enemy("Enemy1", (WINDOWS_WIDTH + 10, random.randint(0 + 40, WINDOWS_HEIGHT - 40)))

            case "Enemy2":
                return Enemy("Enemy2", (WINDOWS_WIDTH + 10, random.randint(0 + 40, WINDOWS_HEIGHT - 40)))
