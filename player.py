from score import Score
import pygame
from colors import *
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT // 4 - 20
        self.change_y = 0
        self.init_change_y = 5
        self.verify_count = 0
        self.score = Score()

    def update(self):
        keys = pygame.key.get_pressed()
        if self.rect.y == (HEIGHT // 4 - 20) or self.rect.y == (3 * HEIGHT // 4 - 20):
            if self.verify_count == 0:
                self.verify_count += 1
                self.score.addPoint()
            if keys[pygame.K_UP] and self.rect.y == (3 * HEIGHT // 4 - 20):
                self.change_y = -self.init_change_y
            if keys[pygame.K_DOWN] and self.rect.y == (HEIGHT // 4 - 20):
                self.change_y = self.init_change_y
        else:
            self.verify_count = 0
            if keys[pygame.K_UP]:
                aux = self.change_y
                self.change_y -= 1
                if self.change_y == 0:
                    self.change_y = aux
            if keys[pygame.K_DOWN]:
                aux = self.change_y
                self.change_y += 1
                if self.change_y == 0:
                    self.change_y = aux
        self.rect.y += self.change_y
        self.rect.y = max(self.rect.y, (HEIGHT // 4 - 20))
        self.rect.y = min(self.rect.y, (3 * HEIGHT // 4 - 20))