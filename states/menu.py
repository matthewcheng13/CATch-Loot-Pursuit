import pygame
from GameState import GameState

def menu_screen(screen, username, SCREEN_WIDTH, SCREEN_HEIGHT):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Constants for screen dimensions and fonts
    font = pygame.font.Font(None, 36)

    # Button
    play_button = pygame.Rect(300, 300, 200, 50)
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
                elif logout_button.collidepoint(event.pos):  # Handle the "Logout" button
                    return GameState.START
                elif quit_button.collidepoint(event.pos):  # Handle the "Quit" button
                    pygame.quit()
        screen.fill(WHITE)

        # Display username at the top of the screen
        username_text = font.render(f"Welcome, {username}!", True, BLACK)
        screen.blit(username_text, (50, 50))

        # Draw the "Play" button
        pygame.draw.rect(screen, BLACK, play_button)
        play_text = font.render("Play", True, WHITE)
        screen.blit(play_text, (play_button.x + 20, play_button.y + 10))
        pygame.draw.rect(screen, BLACK, logout_button)
        logout_text = font.render("Logout", True, WHITE)
        screen.blit(logout_text, (logout_button.x + 20, logout_button.y + 10))
        pygame.draw.rect(screen, BLACK, quit_button)
        quit_text = font.render("Quit", True, WHITE)
        screen.blit(quit_text, (quit_button.x + 20, quit_button.y + 10))

        pygame.display.flip()