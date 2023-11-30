import pygame
import random
import sys
from background import *
from player import Player
from cops import enemies

pygame.init()

#create screen
lvl1 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding a player on the screen')
backgroundmusic = pygame.mixer.Sound("assets/sound/The-Pink-Panther-Theme-Song.mp3")

#clock object
clock = pygame.time.Clock()
#create a player
player = Player(0, SCREEN_HEIGHT-TILE_SIZE*5)
add_enemies(4)
#Main Loop
running = True
background = screen.copy()
draw_background(background)
while running:
    milliseconds = pygame.time.get_ticks()
    elapsed_seconds = (milliseconds - prev_seconds) // 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if elapsed_seconds >= 1:
            timer_value -= 1
            rev_seconds = milliseconds
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
    if elapsed_seconds >= 1:
        timer_value -= 1
        prev_seconds = milliseconds
    if timer_value <= 0:
        running = False
    pygame.mixer.Sound.play(backgroundmusic)
    lvl1.blit(background, (0, 0))
    timer_text = custom_font.render(f"Time left: {timer_value}", True,timer_color )
    text_rect = timer_text.get_rect(center=(SCREEN_WIDTH-950, SCREEN_HEIGHT-550))
    lvl1.blit(timer_text, text_rect)

    player.update()
    enemies.update()
    player.draw(screen)
    enemies.draw(screen)
    clock.tick(60)
    pygame.display.flip()


pygame.quit()