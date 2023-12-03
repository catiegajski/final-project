import random

import pygame
import sys
from cops import *

#Initialize pygame
pygame.init()

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600
TILE_SIZE = 64

MIN_SPEED = 0.5
MAX_SPEED = 3.0
PLAYER_SPEED = 5.0

#create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('THI3F')

caught_sound = pygame.mixer.Sound("assets/sound/caught.mp3")

#load our game font
custom_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf", 50)
score_font = pygame.font.Font("assets/fonts/branda-font.zip", 48)
##Creating a countdown timer
timer_value = 35
timer_color = (255,0,0)
prev_seconds = pygame.time.get_ticks()

#define a function to draw background

def draw_background(lvl1):
    #load our tiles
    sky = pygame.image.load("assets/sprites/starrynight.jpg").convert()
    grass = pygame.image.load("assets/sprites/mapTile_007.png").convert()
    grasssquare = pygame.image.load("assets/sprites/mapTile_010.png").convert()
    outterbank = pygame.image.load("assets/sprites/bank.png").convert()
    #use png transparency
    grass.set_colorkey((0,0,0))
    outterbank.set_colorkey((0,0,0))

    #fill the screen
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            lvl1.blit(sky, (x,y))

    #draw the grass bottom
    for x in range(0,SCREEN_WIDTH, TILE_SIZE):
        lvl1.blit(grass, (x, SCREEN_HEIGHT-TILE_SIZE*4))
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        lvl1.blit(grasssquare, (x, SCREEN_HEIGHT-TILE_SIZE))
    for x in range(0, SCREEN_WIDTH,TILE_SIZE):
        lvl1.blit(grasssquare, (x, SCREEN_HEIGHT-TILE_SIZE*2))
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        lvl1.blit(grasssquare, (x, SCREEN_HEIGHT - TILE_SIZE * 3))
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        lvl1.blit(outterbank, (SCREEN_WIDTH-TILE_SIZE*3, SCREEN_HEIGHT - TILE_SIZE*6))



    #draw the text
        text = custom_font.render("THI3F", True, (255, 0, 0))
        lvl1.blit(text, (SCREEN_WIDTH/2 - text.get_width()/2, (SCREEN_HEIGHT-550)-text.get_height()/2))
def add_enemies(num_ememies):
    for _ in range(num_ememies):
        enemies.add(Enemy(random.randint(SCREEN_WIDTH, SCREEN_WIDTH +20),
                        random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))



