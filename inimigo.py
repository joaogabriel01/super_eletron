import pygame
from cores import *
from configuracoes import *
import random


class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image.fill(VERMELHO)
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(ALTURA // 4 + 80, 3 * (ALTURA // 4) - 80)
        self.rect.x = LARGURA
        self.speed = random.randint(3, 6)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.kill()