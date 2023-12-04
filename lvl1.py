import pygame
import random
import sys
from background import *
from player import Player
from cops import enemies
from rock import *
#from lvl2 import *

pygame.init()
pygame.mixer.init()

#create screen
lvl1 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding a player on the screen')
#sounds and volume
backgroundmusic = pygame.mixer.Sound("assets/sound/The-Pink-Panther-Theme-Song.mp3")
transition_noise = pygame.mixer.Sound("assets/sound/transition.mp3")
pygame.mixer.Sound.play(backgroundmusic)
#Doug Moloney helped me figure out how to have background music and effects
backgroundmusic.set_volume(1)
caught_sound.set_volume(1)

#clock object
clock = pygame.time.Clock()
#create a player
player = Player(0, SCREEN_HEIGHT-TILE_SIZE*5)
add_enemies(4)
add_rocks(3)
#Main Loop
running = True
background = screen.copy()
draw_background(background)

while lives > 0 and running:
    milliseconds = pygame.time.get_ticks()
    elapsed_seconds = (milliseconds - prev_seconds) // 1000
    caught = pygame.sprite.spritecollide(player, enemies, True)
    trip = pygame.sprite.spritecollide(player, rocks, True)
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
    if elapsed_seconds >= 1:
        timer_value -= 1
        prev_seconds = milliseconds
    if elapsed_seconds > timer_value:
        running = False
    if caught:
        pygame.mixer.Sound.play(caught_sound)
        lives -= len(caught)
    if trip:
        PLAYER_SPEED = PLAYER_SPEED*0.1
        #pygame.mixer.Sound.play(caught_sound)
    if player.x == SCREEN_WIDTH - 2*TILE_SIZE:
        pygame.mixer.Sound.play(transition_noise)
        from lvl2 import *
    for ops in enemies:
        if ops.rect.x < -ops.rect.width:  # use the tile size
            enemies.remove(ops)  # remove the fish from the sprite group
            enemies.add(Enemy(random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 50),
                              random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))
    #adding text on multiple screens
    lvl1.blit(background, (0, 0))
    timer_text = custom_font.render(f"Time left: {timer_value}", True, timer_color)
    text_rect = timer_text.get_rect(center=(SCREEN_WIDTH - 950, SCREEN_HEIGHT - 550))
    lvl1.blit(timer_text, text_rect)
    lives_text = custom_font.render(f"Lives left: {lives}", True, timer_color)
    lvl1.blit(lives_text, (SCREEN_WIDTH-675, SCREEN_HEIGHT-525))
    player.update()
    enemies.update()
    rocks.update()
    player.draw(screen)
    enemies.draw(screen)
    rocks.draw(screen)
    clock.tick(60)
    pygame.display.flip()
#change background
lvl1.blit(background, (0, 0))
#print end game message, Jon Briggs helped with game over screen
message = custom_font.render("GAME OVER!", True, (255, 0, 0))
lvl1.blit(message, (SCREEN_WIDTH-675, SCREEN_HEIGHT-500))
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Quit pygame
            pygame.quit()
            sys.exit()