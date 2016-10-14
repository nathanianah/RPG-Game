import pygame
from h import *

class Character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("../res/person.png")
        self.image.set_colorkey(white)

        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 400

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)

        self.direction = direction

        self.image = pygame.image.load("../res/bullet.png")
        self.image.set_colorkey(white)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
