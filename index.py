import pygame
import random

from player import Player
from enemy import Enemy
from colors import *
from settings import *

def menu():
    global running, state
    while state == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    state = "play"

        screen.fill(WHITE)
        font = pygame.font.SysFont(None, 50)
        text = font.render("Press SPACE to play", True, BLUE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
        clock.tick(60)

def play():
    global running, score, state
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    enemies = pygame.sprite.Group()
    while state == "play":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        all_sprites.update()
        enemies.update()
        # Generate enemies randomly
        if random.randrange(100) < 3:  # 3% chance per frame
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)
        # Check collisions
        hits = pygame.sprite.spritecollide(player, enemies, False)
        if hits:
            state = "menu"  # Return to menu after death
        screen.fill(WHITE)
        pygame.draw.rect(screen, GRAY, [0, HEIGHT // 4 - 20, WIDTH, 40])  # Upper platform
        pygame.draw.rect(screen, GRAY, [0, 3 * HEIGHT // 4 - 20, WIDTH, 40])  # Lower platform
        all_sprites.draw(screen)
        font = pygame.font.SysFont(None, 35)
        text = font.render("Score: " + str(player.score.point), True, BLUE)
        screen.blit(text, (10, 10))
        pygame.display.flip()
        clock.tick(60)

# State variables
state = "menu"
running = True
score = 0

# Main loop
while running:
    if state == "menu":
        menu()
    elif state == "play":
        play()

pygame.quit()
