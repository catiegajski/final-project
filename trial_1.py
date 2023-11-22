import pygame
import random
import sys
from background import *
from player import Player

pygame.init()

#create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding a player on the screen')

#clock object
clock = pygame.time.Clock()

#Main Loop
running = True
background = screen.copy()
draw_background(background)

#create a player fish
player = Player(0, SCREEN_HEIGHT-TILE_SIZE*5)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #control fish with keyboard
        if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_w:
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key == pygame.K_DOWN:
            #if event.key == pygame.K_s:
                player.move_down()
            if event.key == pygame.K_LEFT:
            #if event.key == pygame.K_a:
                player.move_left()
            if event.key == pygame.K_RIGHT:
            #if event.key == pygame.K_d:
                player.move_right()
        if event.type == pygame.KEYUP:
            player.stop()

    screen.blit(background, (0, 0))
    player.update()

    player.draw(screen)

    clock.tick(60)

    pygame.display.flip()
pygame.quit()
