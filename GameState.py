from enum import Enum

class GameState(Enum):
    START = 0
    MENU = 1
    WORLDS = 2
    WORLD = 3
    LEVEL_OPTIONS = 4
    LEVEL = 5
    COLLECTION = 6
    ACHIEVEMENTS = 7
    CAT = 8