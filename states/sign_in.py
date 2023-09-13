import pygame
from GameState import GameState
from sql import create_user, verify_user

def sign_in_screen(screen, login, SCREEN_WIDTH, SCREEN_HEIGHT):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    font = pygame.font.Font(None, 36)

    # text input fields
    username_input = pygame.Rect(300, 200, 200, 36)
    password_input = pygame.Rect(300, 300, 200, 36)
    username_text = ''
    password_text = ''
    input_active = 'username'

    # buttons
    button = pygame.Rect(300, 400, 100, 50)
    back_button = pygame.Rect(50, 500, 100, 50)

    # messages
    error_message = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return GameState.START
            if event.type == pygame.MOUSEBUTTONDOWN:
                if username_input.collidepoint(event.pos):
                    input_active = "username"
                elif password_input.collidepoint(event.pos):
                    input_active = "password"
                else:
                    input_active = False
                if button.collidepoint(event.pos):
                    if login:
                        success = verify_user(username_text, password_text)
                        if success:
                            return username_text
                        else:
                            error_message = "Incorrect username or password."
                    else:
                        if username_text and password_text:
                            create_user(username_text, password_text)
                            return username_text
                    print("Button clicked")
                elif back_button.collidepoint(event.pos):  # Handle the "Back" button
                    return ""
            if event.type == pygame.KEYDOWN:
                if input_active == 'username':
                    if event.key == pygame.K_RETURN:
                        if login:
                            success = verify_user(username_text, password_text)
                            if success:
                                return username_text
                            else:
                                error_message = "Incorrect username or password."
                        else:
                            if username_text and password_text:
                                create_user(username_text, password_text)
                                return username_text
                        print("Button clicked")
                    elif event.key == pygame.K_BACKSPACE:
                        username_text = username_text[:-1]
                    elif event.key == pygame.K_TAB:
                        input_active = 'password'
                    else:
                        username_text += event.unicode
                elif input_active == 'password':
                    if event.key == pygame.K_RETURN:
                        if login:
                            success = verify_user(username_text, password_text)
                            if success:
                                return username_text
                            else:
                                error_message = "Incorrect username or password."
                        else:
                            if username_text and password_text:
                                create_user(username_text, password_text)
                                return username_text
                    elif event.key == pygame.K_BACKSPACE:
                        password_text = password_text[:-1]
                    elif event.key == pygame.K_TAB:
                        # do nothing
                        pass
                    else:
                        password_text += event.unicode

        screen.fill(WHITE)

        # Draw text input fields
        pygame.draw.rect(screen, BLACK, username_input, 2)
        pygame.draw.rect(screen, BLACK, password_input, 2)
        username_text_surface = font.render(username_text, True, BLACK)
        password_text_surface = font.render(password_text, True, BLACK)
        screen.blit(username_text_surface, (username_input.x + 5, username_input.y + 5))
        screen.blit(password_text_surface, (password_input.x + 5, password_input.y + 5))

        # Draw buttons
        pygame.draw.rect(screen, BLACK, button)
        button_text = font.render("Login" if login else "Register", True, WHITE)
        screen.blit(button_text, (button.x + 20, button.y + 10))
        pygame.draw.rect(screen, BLACK, back_button)
        back_button_text = font.render("Back", True, WHITE)
        screen.blit(back_button_text, (back_button.x + 20, back_button.y + 10))

        # Draw error messages
        error_text = font.render(error_message, True, (255, 0, 0))
        screen.blit(error_text, (300, 500))

        pygame.display.flip()