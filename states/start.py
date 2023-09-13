import pygame
from GameState import GameState
from states.sign_in import sign_in_screen

def start_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Fonts
    font = pygame.font.Font(None, 36)

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

        # Draw buttons
        pygame.draw.rect(screen, BLACK, login_button)
        pygame.draw.rect(screen, BLACK, register_button)
        login_text = font.render("Login", True, WHITE)
        register_text = font.render("Register", True, WHITE)
        screen.blit(login_text, (login_button.x + 20, login_button.y + 10))
        screen.blit(register_text, (register_button.x + 10, register_button.y + 10))
        pygame.draw.rect(screen, BLACK, quit_button)
        quit_text = font.render("Quit", True, WHITE)
        screen.blit(quit_text, (quit_button.x + 20, quit_button.y + 10))

        pygame.display.flip()