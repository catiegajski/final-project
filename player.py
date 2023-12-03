
import pygame
from background import *
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.forward_image = pygame.image.load("assets/sprites/thief.png")
        self.reverse_image = pygame.transform.flip(self.forward_image, True, False)
        self.image = self.forward_image
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-150, -100)
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0

    def move_up(self):
        self.y_speed = -1 * PLAYER_SPEED

    def move_down(self):
        self.y_speed = PLAYER_SPEED

    def move_left(self):
        self.x_speed = -1 * PLAYER_SPEED
        self.image = self.reverse_image

    def move_right(self):
        self.x_speed = PLAYER_SPEED
        self.image = self.forward_image

    def stop(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        #print(self.y_speed)
        self.x += self.x_speed
        self.y += self.y_speed #sets the self.y_speed to 0 if non-arrow keys pressed
        #print(self.x, self.y)
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

    def draw(self, lvl1):
        lvl1.blit(self.image, self.rect)