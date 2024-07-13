# COLOR
import pygame

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

# MENU TEXT
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
                "Player1Shot": 2,
                "Player2Shot": 3
                }

ENTITY_HEALTH = {"imagebackground0": 999,
                 "imagebackground1": 999,
                 "imagebackground2": 999,
                 "imagebackground3": 999,
                 "imagebackground4": 999,
                 "imagebackground5": 999,
                 "imagebackground6": 999,
                 "imagebackground7": 999,
                 "Player1": 300,
                 "Player1Shot": 1,
                 "Player2": 300,
                 "Player2Shot": 1,
                 "Enemy1": 100,
                 "Enemy2": 100,
                 }


# Creation time gap shot when the shooting button is pressed
ENTITY_SHOT_DELAY = {"Player1": 20,
                     "Player2": 20
                     }

# PLAYER_KEYBOARD_MOVEMENT
PLAYER_KEY_UP = {"Player1": pygame.K_UP,
                 "Player2": pygame.K_w}

PLAYER_KEY_DOWN = {"Player1": pygame.K_DOWN,
                   "Player2": pygame.K_s}

PLAYER_KEY_RIGHT = {"Player1": pygame.K_RIGHT,
                    "Player2": pygame.K_d}

PLAYER_KEY_LEFT = {"Player1": pygame.K_LEFT,
                   "Player2": pygame.K_a}

PLAYER_KEY_SHOOT = {"Player1": pygame.K_RCTRL,
                    "Player2": pygame.K_LCTRL}

#EVENT ENEMY
EVENT_ENEMY = pygame.USEREVENT + 1
