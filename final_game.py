import pygame
import sys

pygame.init()

# Set up the screen
startmenu = pygame.display.set_mode((1100, 600))
pygame.display.set_caption('Pygame Start Menu')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Fonts
custom_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf", 60)

box_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf", 25)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


while True:
    startmenu.fill(BLACK)
    draw_text('THI3F', custom_font, RED, startmenu, 500, 50)

    mouse_pos = pygame.mouse.get_pos()

        # Start Game button
    start_game_rect = pygame.Rect(475, 200, 200, 50)
    pygame.draw.rect(startmenu, WHITE, start_game_rect)
    draw_text('Start Game', box_font, BLACK, startmenu, 500, 215)

        # Quit button
    quit_rect = pygame.Rect(475, 300, 200, 50)
    pygame.draw.rect(startmenu, WHITE, quit_rect)
    draw_text('Quit', box_font, BLACK, startmenu, 530, 310)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_game_rect.collidepoint(mouse_pos):
                from lvl1 import *
            elif quit_rect.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()

    pygame.display.update()


