
import pygame
import random
from background import *

class Rock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/rock.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x,y)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, lvl2):
        lvl2.blit(self.image, self.rect)

rocks = pygame.sprite.Group()