
import pygame
import random
from background import *

class Money(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/money.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (115,115))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x,y)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x
        if self.x > SCREEN_WIDTH- 2*TILE_SIZE:
            self.x = SCREEN_WIDTH - 2*TILE_SIZE
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.y > SCREEN_HEIGHT - TILE_SIZE :
            self.y = (SCREEN_HEIGHT-TILE_SIZE)
        #Doug Moloney Helped me limit the top restriction :)
        if self.y < SCREEN_HEIGHT-5*TILE_SIZE:
            self.y = (SCREEN_HEIGHT-5*TILE_SIZE)
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.center = (self.x, self.y)


    def draw(self, lvl2):
        lvl2.blit(self.image, self.rect)

moneys = pygame.sprite.Group()