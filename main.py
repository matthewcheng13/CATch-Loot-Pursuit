import pygame
import sqlite3
from GameState import GameState
from states.start import start_screen
from states.menu import menu_screen

pygame.init()

# window dimensions
screen_width = 800
screen_height = 600

# create game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("CATch, Loot: Pursuit")

running = True
current_state = GameState.START
user = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # game logic
    if current_state == GameState.START:
        # Handle the start screen
        # Transition to MENU or handle user registration/login
        user = start_screen(screen, screen_width, screen_height)
        current_state = GameState.MENU
    elif current_state == GameState.MENU:
        # Handle the main menu
        # Transition to WORLDS or other menu options
        if user is not None:
            current_state = menu_screen(screen, user, screen_width, screen_height)
            if current_state == GameState.START:
                user = None
    elif current_state == GameState.WORLDS:
        # Handle world selection screen
        # Transition to WORLD based on user selection
        running = False

    elif current_state == GameState.WORLD:
        # Handle the world map
        # Transition to LEVEL_OPTIONS or other world interactions
        pass

    elif current_state == GameState.LEVEL_OPTIONS:
        # Handle level options screen
        # Transition to LEVEL when the player starts the game
        pass

    elif current_state == GameState.LEVEL:
        # Handle the game level
        # Transition back to WORLD when the level is completed or other game actions
        pass

    # Other game logic for each state

    pygame.display.update()

pygame.quit()