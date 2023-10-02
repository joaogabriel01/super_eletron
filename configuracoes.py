import pygame

# Inicializar pygame
pygame.init()

info_object = pygame.display.Info()
LARGURA = info_object.current_w
ALTURA = info_object.current_h

# Criação da tela e relógio
tela = pygame.display.set_mode((LARGURA, ALTURA), pygame.FULLSCREEN)
pygame.display.set_caption("SUPER ELETRON")
relogio = pygame.time.Clock()