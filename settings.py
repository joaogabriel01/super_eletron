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