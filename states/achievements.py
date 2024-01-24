import pygame
from GameState import GameState

def achievements_screen(screen, username, SCREEN_WIDTH, SCREEN_HEIGHT):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Constants for screen dimensions and fonts
    fonts = pygame.font.Font(None, 36)
    fontl = pygame.font.Font(None, 72)

    # Button
    play_button = pygame.Rect(300, 200, 200, 100)
    collection_button = pygame.Rect(300, 325, 200, 50)
    achievements_button = pygame.Rect(300, 400, 200, 50)
    logout_button = pygame.Rect(600, 50, 100, 50) 
    quit_button = pygame.Rect(600, 500, 100, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return GameState.START
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    # Transition to the WORLDS screen when "Play" is clicked
                    return GameState.WORLDS
                elif collection_button.collidepoint(event.pos):
                    return GameState.COLLECTION
                elif achievements_button.collidepoint(event.pos):
                    return GameState.ACHIEVEMENTS
                elif logout_button.collidepoint(event.pos):  # Handle the "Logout" button
                    return GameState.START
                elif quit_button.collidepoint(event.pos):  # Handle the "Quit" button
                    pygame.quit()
        screen.fill(WHITE)

        # Display username at the top of the screen
        username_text = fonts.render(f"Welcome, {username}!", True, BLACK)
        screen.blit(username_text, (50, 50))

        # Draw the "Play" button
        pygame.draw.rect(screen, BLACK, play_button)
        play_text = fontl.render("Play", True, WHITE)
        screen.blit(play_text, (play_button.x + 48, play_button.y + 25))
        pygame.draw.rect(screen, BLACK, collection_button)
        collection_text = fonts.render("Collection", True, WHITE)
        screen.blit(collection_text, (collection_button.x + 35, collection_button.y + 10))
        pygame.draw.rect(screen, BLACK, achievements_button)
        achievements_text = fonts.render("Achievements", True, WHITE)
        screen.blit(achievements_text, (achievements_button.x + 15, achievements_button.y + 10))
        pygame.draw.rect(screen, BLACK, logout_button)
        logout_text = fonts.render("Logout", True, WHITE)
        screen.blit(logout_text, (logout_button.x + 8, logout_button.y + 10))
        pygame.draw.rect(screen, BLACK, quit_button)
        quit_text = fonts.render("Quit", True, WHITE)
        screen.blit(quit_text, (quit_button.x + 20, quit_button.y + 10))

        pygame.display.flip()