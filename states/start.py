import pygame
from GameState import GameState
from states.sign_in import sign_in_screen

def start_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Fonts
    fonts = pygame.font.Font(None, 36)
    fontl = pygame.font.Font(None, 72)

    # Buttons
    login_button = pygame.Rect(300, 300, 200, 50)
    register_button = pygame.Rect(300, 400, 200, 50)
    quit_button = pygame.Rect(600, 500, 100, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return GameState.START
            if event.type == pygame.MOUSEBUTTONDOWN:
                if login_button.collidepoint(event.pos):
                    # Transition to the sign-in screen for login
                    ret = sign_in_screen(screen, True, SCREEN_WIDTH, SCREEN_HEIGHT)
                    if ret:
                        return ret
                elif register_button.collidepoint(event.pos):
                    # Transition to the sign-in screen for registration
                    ret = sign_in_screen(screen, False, SCREEN_WIDTH, SCREEN_HEIGHT)
                    if ret:
                        return ret
                elif quit_button.collidepoint(event.pos):  # Handle the "Quit" button
                    pygame.quit()
        screen.fill(WHITE)

        # Draw text
        text = fontl.render("CATch, Loot: PURRsuit", True, (0,0,0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        screen.blit(text, text_rect)

        # Draw buttons
        pygame.draw.rect(screen, BLACK, login_button)
        pygame.draw.rect(screen, BLACK, register_button)
        login_text = fonts.render("Login", True, WHITE)
        register_text = fonts.render("Register", True, WHITE)
        screen.blit(login_text, (login_button.x + 63, login_button.y + 10))
        screen.blit(register_text, (register_button.x + 50, register_button.y + 10))
        pygame.draw.rect(screen, BLACK, quit_button)
        quit_text = fonts.render("Quit", True, WHITE)
        screen.blit(quit_text, (quit_button.x + 20, quit_button.y + 10))

        pygame.display.flip()