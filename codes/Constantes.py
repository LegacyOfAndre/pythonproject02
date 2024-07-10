# COLOR
import pygame

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

# MENUTEXT
MENU_OPTION = ("New Game 1 Player",
               "New Game 2 Players - Cooperative",
               "New Game 2 Players - Competitive",
               "Exit")
# WINDOW
WINDOWS_WIDTH = 576
WINDOWS_HEIGHT = 324

# E
ENTITY_SPEED = {"imagebackground0": 0,
                "imagebackground1": 1,
                "imagebackground2": 2,
                "imagebackground3": 3,
                "imagebackground4": 4,
                "imagebackground5": 5,
                "imagebackground6": 6,
                "imagebackground7": 7,
                "Player1": 2.5,
                "Player2": 3,
                "Enemy1": 2.5,
                "Enemy2": 2.0,
                }

#PLAYER_KEYBOARD_MOVEMENT
PLAYER_KEY_UP = {"Player1": pygame.K_UP,
                 "Player2": pygame.K_w}

PLAYER_KEY_DOWN = {"Player1": pygame.K_DOWN,
                   "Player2": pygame.K_s}

PLAYER_KEY_RIGHT = {"Player1": pygame.K_RIGHT,
                    "Player2": pygame.K_d}

PLAYER_KEY_LEFT = {"Player1": pygame.K_LEFT,
                   "Player2": pygame.K_a}

#EVENT ENEMY
EVENT_ENEMY = pygame.USEREVENT + 1
