import random

import pygame
import sys
from cops import *
from money import *

#Initialize pygame
pygame.init()

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600
TILE_SIZE = 64

MIN_SPEED = 0.5
MAX_SPEED = 3.0
PLAYER_SPEED = 5.0

lives = 2

#create screen
lvl2 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('THI3F: LEVEL II')


caught_sound = pygame.mixer.Sound("assets/sound/caught.mp3")

#load our game font
custom_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf", 50)
##Creating a countdown timer
timer_value = 35
timer_color = (255,0,0)
prev_seconds = pygame.time.get_ticks()

score = 0
score_font = pygame.font.Font("assets/fonts/branda-font.zip", 48)

#define a function to draw background

def draw_background(lvl2):
    #load our tiles
    insidebank = pygame.image.load("assets/sprites/insidebank.jfif").convert()
    floor = pygame.image.load("assets/sprites/carpet.jpg")
    pygame.transform.scale(floor, (64, 64))
    door = pygame.image.load("assets/sprites/bank.png").convert()
    #use png transparency
    floor.set_colorkey((0,0,0))
    door.set_colorkey((0,0,0))

    #fill the screen
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            lvl2.blit(insidebank, (x,y))

    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        lvl2.blit(floor, (x, SCREEN_HEIGHT-TILE_SIZE))
    for x in range(0, SCREEN_WIDTH,TILE_SIZE):
        lvl2.blit(floor, (x, SCREEN_HEIGHT-TILE_SIZE*2))
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        lvl2.blit(floor, (x, SCREEN_HEIGHT - TILE_SIZE * 3))
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        lvl2.blit(floor, (x, SCREEN_HEIGHT - TILE_SIZE * 4))

    #draw the text
        text = custom_font.render("THI3F: LVL II", True, (255, 0, 0))
        lvl2.blit(text, (SCREEN_WIDTH/2 - text.get_width()/2, (SCREEN_HEIGHT-550)-text.get_height()/2))

def add_enemies(num_ememies):
    for _ in range(num_ememies):
        enemies.add(Enemy(random.randint(SCREEN_WIDTH, SCREEN_WIDTH +20),
                        random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))

def add_money(num_money):
    for _ in range(num_money):
        moneys.add(Money(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 1.5),
                        random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))
