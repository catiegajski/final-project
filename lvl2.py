import pygame
import random
import sys
from background_lvl2 import *
from player import Player

pygame.init()

#create screen
lvl2 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding a player on the screen')
backgroundmusic = pygame.mixer.Sound("assets/sound/The-Pink-Panther-Theme-Song.mp3")
money_noise = pygame.mixer.Sound("assets/sound/money_noise.mp3")

#clock object
clock = pygame.time.Clock()
#create a player
player = Player(0, SCREEN_HEIGHT-TILE_SIZE*5)
add_enemies(3)
add_money(6)
#Main Loop
running = True
background = lvl2.copy()
draw_background(background)
while running:
    milliseconds = pygame.time.get_ticks()
    elapsed_seconds = (milliseconds - prev_seconds) // 1000
    caught = pygame.sprite.spritecollide(player, enemies, True)
    gains = pygame.sprite.spritecollide(player, moneys, True)
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
        running = False
    if gains:
        pygame.mixer.Sound.play(money_noise)
        score += len(gains)
        for _ in range(len(gains)):
            moneys.add(Money(random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 20),random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))
    for cash in moneys:
        if cash.rect.x < -cash.rect.width:  # use the tile size
            moneys.remove(cash)  # remove the fish from the sprite group
            moneys.add(Money(random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 50),
                            random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))
    for ops in enemies:
        if ops.rect.x < -ops.rect.width:  # use the tile size
            enemies.remove(ops)  # remove the fish from the sprite group
            enemies.add(Enemy(random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 50),
                            random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))
    pygame.mixer.Sound.play(backgroundmusic)
    lvl2.blit(background, (0, 0))
    score_text = custom_font.render(f"Score: {score}", True, timer_color)
    lvl2.blit(score_text, (SCREEN_WIDTH - 250, SCREEN_HEIGHT - 600))
    timer_text = custom_font.render(f"Time left: {timer_value}", True,timer_color )
    text_rect = timer_text.get_rect(center=(SCREEN_WIDTH-950, SCREEN_HEIGHT-550))
    lvl2.blit(timer_text, text_rect)
    lives_text = custom_font.render(f"Lives left: {lives}", True, timer_color)
    lvl2.blit(lives_text, (SCREEN_WIDTH - 675, SCREEN_HEIGHT - 525))

    player.update()
    enemies.update()
    moneys.update()
    player.draw(lvl2)
    enemies.draw(lvl2)
    moneys.draw(lvl2)
    clock.tick(60)
    pygame.display.flip()

lvl2.blit(background, (0, 0))
#print end game message, Jon Briggs helped with game over screen
message = custom_font.render("GAME OVER!", True, (255, 0, 0))
lvl2.blit(message, (SCREEN_WIDTH-675, SCREEN_HEIGHT-500))
score_text = custom_font.render(f"Score: {score}", True, timer_color)
lvl2.blit(score_text, (SCREEN_WIDTH -675, SCREEN_HEIGHT -400))
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Quit pygame
            pygame.quit()
            sys.exit()


pygame.quit()