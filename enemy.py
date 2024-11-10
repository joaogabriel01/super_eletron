import pygame
from colors import *
from settings import *
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(HEIGHT // 4 + 80, 3 * (HEIGHT // 4) - 80)
        self.rect.x = WIDTH
        self.speed = random.randint(3, 6)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.kill()