import pygame

# Initialize pygame
pygame.init()

info_object = pygame.display.Info()
WIDTH = info_object.current_w
HEIGHT = info_object.current_h

# Create screen and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("SUPER ELECTRON")
clock = pygame.time.Clock()

# Constants
UPPER_PLATFORM_Y = HEIGHT // 4 - 20
LOWER_PLATFORM_Y = 3 * HEIGHT // 4 - 20
PLAYER_SIZE = 40
ENEMY_SIZE = 40
ENEMY_SPAWN_CHANCE = 3  # 3% chance per frame